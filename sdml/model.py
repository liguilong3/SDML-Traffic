import random
import numpy as np
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import Dataset

W = 3
TOP_K_POSITIVE = 5
LEARNABLE_PROMPT_DIM = 10
ADAPTER_OUT_DIM = 12
STATE_DIM = 12
BEHAVIOR_DIM = 24
DROPOUT_RATE = 0.2

class TemporalQueryDataset(Dataset):
    def __init__(self, state_obs, list_of_times, window: int = W, top_k_pos: int = TOP_K_POSITIVE):
        self.state_obs = state_obs
        self.N_obs, self.T = state_obs.shape
        self.window = window
        self.top_k_pos = top_k_pos
        self.times = list_of_times
        self.local_idxs = list(range(self.N_obs))
        self.positive_pools = {}
        for t in self.times:
            seq_all = self.state_obs[:, t - self.window + 1:t + 1]
            diffs = np.linalg.norm(seq_all[None, :, :] - seq_all[:, None, :], axis=2)
            order = np.argsort(diffs, axis=1)
            others = order[order != np.arange(self.N_obs)[:, None]].reshape(self.N_obs, self.N_obs - 1)
            self.positive_pools[t] = others[:, :self.top_k_pos]

    def __len__(self) -> int:
        return len(self.times) * self.N_obs

    def __getitem__(self, idx):
        t = random.choice(self.times)
        q_local = random.choice(self.local_idxs)
        valid_pool = self.positive_pools[t][q_local]
        pos_local = random.choice(valid_pool) if len(valid_pool) > 0 else q_local
        return {"q_local": int(q_local), "t": int(t), "pos_local": int(pos_local)}

def collate_fn(samples):
    return {
        "q_local": torch.tensor([s["q_local"] for s in samples], dtype=torch.long),
        "t": torch.tensor([s["t"] for s in samples], dtype=torch.long),
        "pos_local": torch.tensor([s["pos_local"] for s in samples], dtype=torch.long),
    }

class AdapterV10_Gated(nn.Module):
    def __init__(
        self,
        frozen_embeds_np,
        learnable_dim: int = LEARNABLE_PROMPT_DIM,
        out_dim: int = ADAPTER_OUT_DIM,
        dropout: float = DROPOUT_RATE,
    ):
        super().__init__()
        self.register_buffer("frozen_embeds", torch.from_numpy(frozen_embeds_np).float())
        self.learnable_prompt = nn.Parameter(torch.randn(1, learnable_dim) * 0.02)
        self.v_proj = nn.Linear(frozen_embeds_np.shape[1], out_dim)
        self.gate_proj = nn.Linear(learnable_dim, out_dim)
        self.final_norm = nn.LayerNorm(out_dim)
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, indices):
        b = indices.shape[0]
        v = self.dropout(self.v_proj(self.frozen_embeds[indices]))
        z = torch.sigmoid(self.gate_proj(self.learnable_prompt.repeat(b, 1)))
        s_refined = (1 - z) * v + z * torch.tanh(v)
        return self.final_norm(s_refined)

class StateEncoder(nn.Module):
    def __init__(self, in_window: int = W, out_dim: int = STATE_DIM, dropout: float = DROPOUT_RATE):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_window, out_dim * 2),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            nn.LayerNorm(out_dim * 2),
            nn.Linear(out_dim * 2, out_dim),
        )

    def forward(self, s_with_mask):
        values, masks = s_with_mask[:, 0, :, :], s_with_mask[:, 1, :, :]
        mean_profile = torch.sum(values, dim=2) / (torch.sum(masks, dim=2) + 1e-6)
        return self.net(mean_profile)

class BehaviorNet(nn.Module):
    def __init__(
        self,
        s_dim: int = ADAPTER_OUT_DIM,
        state_dim: int = STATE_DIM,
        out_dim: int = BEHAVIOR_DIM,
        dropout: float = DROPOUT_RATE,
    ):
        super().__init__()
        in_dim = s_dim + state_dim
        self.linear_path = nn.Linear(in_dim, out_dim)
        self.residual_path = nn.Sequential(
            nn.Linear(in_dim, 64),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            nn.Linear(64, out_dim),
        )
        self.alpha = nn.Parameter(torch.zeros(1))

    def forward(self, s, h):
        x = torch.cat([s, h], dim=-1)
        out = self.linear_path(x) + self.alpha * self.residual_path(x)
        return F.normalize(out, dim=-1)


def build_state_batch_with_mask(state_obs_arr, times, window, observed_masks):
    indices = np.asarray(times)[:, None] - window + 1 + np.arange(window)[None, :]
    values = state_obs_arr[:, indices].transpose(1, 2, 0)
    masks = np.broadcast_to(observed_masks[:, None, :], values.shape)
    return np.stack([(values * masks).astype(np.float32), masks.astype(np.float32)], axis=1)
