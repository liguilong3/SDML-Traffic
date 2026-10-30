from pathlib import Path
import csv
import json
import random
import time
import numpy as np
import torch
from torch.nn import functional as F
from torch.utils.data import DataLoader
from tqdm import tqdm
from .model import (AdapterV10_Gated, StateEncoder, BehaviorNet,
                    TemporalQueryDataset, collate_fn, build_state_batch_with_mask)
from .evaluation import predict, scores


class Experiment:
    def __init__(self, document, state, embeddings, device="cpu", smoke=False):
        self.document = document
        self.case, self.cfg = document["case"], dict(document["training"])
        cfg = self.cfg
        self.DEVICE = torch.device("cuda" if device == "auto" and torch.cuda.is_available()
                                   else "cpu" if device == "auto" else device)
        seed = cfg["training_seed"]
        torch.manual_seed(seed)
        np.random.seed(seed)
        random.seed(seed)
        torch.set_num_threads(1)
        self.state, self.static_emb_all = state, embeddings
        self.N, self.T_total = state.shape
        self.observed_idxs = np.asarray(self.case["seen_indices"], dtype=int)
        self.unobserved_idxs = np.asarray(self.case["unseen_indices"], dtype=int)
        self.N_obs, self.N_unobs = len(self.observed_idxs), len(self.unobserved_idxs)
        for attr, key in {"W": "window", "BATCH_QUERIES": "batch_queries", "LR": "lr",
                          "TEMPERATURE": "temperature", "EPOCHS": "epochs", "TOP_K": "top_k",
                          "TOP_K_POSITIVE": "top_k_positive", "STATE_VALUE_SCALE": "state_value_scale",
                          "OBS_MISSING_PROB": "obs_missing_prob", "WEIGHT_DECAY": "weight_decay",
                          "BEHAVIOR_DIM": "behavior_dim"}.items():
            setattr(self, attr, cfg[key])
        self.state_norm = (state / float(self.STATE_VALUE_SCALE)).astype(np.float32)
        self.state_norm_obs = self.state_norm[self.observed_idxs]
        end = int(self.T_total * cfg["train_fraction"])
        self.train_sample_times = list(range(self.W, end))
        self.test_times = list(range(end, self.T_total))
        self.smoke = smoke
        if smoke:
            self.EPOCHS, self.BATCH_QUERIES = 1, 8
            self.train_sample_times = self.train_sample_times[:4]
            self.test_times = self.test_times[:4]

    def modules(self):
        cfg, device = self.cfg, self.DEVICE
        adapter = AdapterV10_Gated(self.static_emb_all,
                                  learnable_dim=cfg["learnable_prompt_dim"],
                                  out_dim=cfg["adapter_out_dim"], dropout=cfg["dropout"]).to(device)
        encoder = StateEncoder(in_window=self.W, out_dim=cfg["state_dim"],
                               dropout=cfg["dropout"]).to(device)
        behavior = BehaviorNet(s_dim=cfg["adapter_out_dim"], state_dim=cfg["state_dim"],
                               out_dim=self.BEHAVIOR_DIM, dropout=cfg["dropout"]).to(device)
        return adapter, encoder, behavior

    @torch.no_grad()
    def train_predictions(self, modules, batch_size=512):
        adapter, encoder, behavior = modules
        for model in modules:
            model.eval()
        times = np.asarray(self.train_sample_times)
        normalized = torch.from_numpy(self.state_norm_obs).to(self.DEVICE)
        windows = normalized.unfold(1, self.W, 1).permute(1, 2, 0).contiguous()
        qs = np.repeat(np.arange(self.N_obs), len(times))
        ts = np.tile(times, self.N_obs)
        result = np.empty((self.N_obs, len(times)), dtype=np.float64)
        semantic = adapter(torch.arange(self.N, device=self.DEVICE))
        nodes = torch.as_tensor(self.observed_idxs, device=self.DEVICE)
        for start in range(0, len(ts), batch_size):
            current, q = ts[start:start + batch_size], qs[start:start + batch_size]
            t = torch.as_tensor(current, device=self.DEVICE)
            qi = torch.as_tensor(q, device=self.DEVICE)
            rows = torch.arange(len(current), device=self.DEVICE)
            values = windows[t - self.W + 1].clone()
            mask = torch.ones_like(values)
            values[rows, :, qi] = 0
            mask[rows, :, qi] = 0
            context = encoder(torch.stack([values, mask], dim=1))
            vectors = behavior(semantic[None].expand(len(current), -1, -1),
                               context[:, None].expand(-1, self.N, -1))
            anchor = vectors[rows, nodes[qi]]
            similarities = torch.bmm(anchor[:, None], vectors[:, nodes].transpose(1, 2)).squeeze(1)
            similarities[rows, qi] = -torch.inf
            chosen = torch.argsort(similarities, dim=1, descending=True, stable=True)[:, :self.TOP_K]
            sim = similarities.gather(1, chosen).double()
            weights = torch.exp(sim / self.TEMPERATURE)
            weights = weights / (weights.sum(1, keepdim=True) + 1e-9)
            donor = normalized[chosen, t[:, None]].double()
            result.reshape(-1)[start:start + len(current)] = (
                (weights * donor).sum(1).cpu().numpy() * self.STATE_VALUE_SCALE)
        return result

    def evaluate(self, modules):
        random_state, numpy_state = random.getstate(), np.random.get_state()
        torch_state = torch.get_rng_state()
        cuda_state = torch.cuda.get_rng_state_all() if torch.cuda.is_available() else None
        try:
            training = self.train_predictions(modules)
            testing = predict(self, *modules, self.test_times)["default"]
            return (scores(self.state[np.ix_(self.observed_idxs, self.train_sample_times)], training),
                    scores(self.state[np.ix_(self.unobserved_idxs, self.test_times)], testing), testing)
        finally:
            random.setstate(random_state)
            np.random.set_state(numpy_state)
            torch.set_rng_state(torch_state)
            if cuda_state is not None:
                torch.cuda.set_rng_state_all(cuda_state)

    def train(self, output_dir):
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        if (output_dir / "history.csv").exists() or (output_dir / "model.pt").exists():
            raise FileExistsError("Choose a new output directory to preserve the previous run.")
        adapter, state_encoder, behavior = modules = self.modules()
        params = list(adapter.parameters()) + list(state_encoder.parameters()) + list(behavior.parameters())
        opt = torch.optim.AdamW(params, lr=self.LR, weight_decay=self.WEIGHT_DECAY)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            opt, T_max=self.cfg.get("scheduler_epochs", self.EPOCHS))
        dataset = TemporalQueryDataset(self.state_norm_obs, self.train_sample_times,
                                       window=self.W, top_k_pos=self.TOP_K_POSITIVE)
        loader = DataLoader(dataset, batch_size=self.BATCH_QUERIES, shuffle=True, collate_fn=collate_fn)
        obs_idxs_gpu = torch.from_numpy(self.observed_idxs).long().to(self.DEVICE)
        history = []
        (output_dir / "config.json").write_text(json.dumps(self.document, indent=2) + "\n")
        for epoch in range(self.EPOCHS):
            started = time.monotonic()
            for model in modules:
                model.train()
            total_loss, batch_count, lr_used = 0.0, 0, opt.param_groups[0]["lr"]
            for batch in tqdm(loader, desc=f"Epoch {epoch + 1}/{self.EPOCHS}", leave=False):
                q_local, times = batch["q_local"].numpy(), batch["t"].numpy()
                pos_local = batch["pos_local"].to(self.DEVICE)
                bsz = len(q_local)
                masks = np.ones((bsz, self.N_obs), dtype=np.float32)
                if self.OBS_MISSING_PROB > 0:
                    masks[np.random.rand(bsz, self.N_obs) < self.OBS_MISSING_PROB] = 0.0
                s_batch = build_state_batch_with_mask(self.state_norm_obs, times, self.W, masks)
                h_batch = state_encoder(torch.from_numpy(s_batch).float().to(self.DEVICE))
                s_all = adapter(torch.arange(self.N, device=self.DEVICE).long())
                s_obs = s_all[obs_idxs_gpu]
                b_all = behavior(s_obs.unsqueeze(0).repeat(bsz, 1, 1),
                                 h_batch.unsqueeze(1).repeat(1, self.N_obs, 1))
                anchor = b_all.gather(1, torch.from_numpy(q_local).long().to(self.DEVICE)
                                     .view(bsz, 1, 1).expand(-1, -1, self.BEHAVIOR_DIM)).squeeze(1)
                logits = torch.bmm(anchor.unsqueeze(1), b_all.transpose(1, 2)).squeeze(1) / self.TEMPERATURE
                loss = F.cross_entropy(logits, pos_local)
                opt.zero_grad()
                loss.backward()
                opt.step()
                total_loss += loss.item()
                batch_count += 1
                if self.smoke and batch_count == 2:
                    break
            scheduler.step()
            training, testing, predictions = self.evaluate(modules)
            record = {"epoch": epoch + 1, "train_loss": total_loss / max(batch_count, 1),
                      "lr_used": lr_used, "alpha": behavior.alpha.item(),
                      **{"train_" + k: v for k, v in training.items()},
                      **{"test_" + k: v for k, v in testing.items()}}
            history.append(record)
            with (output_dir / "history.csv").open("w", newline="") as handle:
                writer = csv.DictWriter(handle, list(record))
                writer.writeheader()
                writer.writerows(history)
            print(f"Epoch {epoch + 1:02d}/{self.EPOCHS}: train MAE={training['mae']:.4f}  "
                  f"MAPE={training['mape']:.2f}%  RMSE={training['rmse']:.4f} "
                  f"({time.monotonic() - started:.1f}s)", flush=True)
        checkpoint = {"config": self.document, "epoch": self.EPOCHS,
                      "adapter": adapter.state_dict(), "state_encoder": state_encoder.state_dict(),
                      "behavior": behavior.state_dict()}
        torch.save(checkpoint, output_dir / "model.pt")
        np.save(output_dir / "test_predictions.npy", predictions, allow_pickle=False)
        (output_dir / "test_node_ids.json").write_text(json.dumps(self.case["unseen_ids"]) + "\n")
        (output_dir / "summary.json").write_text(json.dumps({
            "case": self.case["name"], "seed": self.cfg["training_seed"], "epoch": self.EPOCHS,
            "smoke": self.smoke, "device": str(self.DEVICE), "torch": torch.__version__,
            "train": training, "test": testing}, indent=2) + "\n")
        return history

    def infer(self, checkpoint_path, output_dir):
        checkpoint = torch.load(checkpoint_path, map_location=self.DEVICE, weights_only=True)
        if checkpoint["config"] != self.document:
            raise ValueError("The checkpoint configuration must match --config.")
        modules = self.modules()
        for model, key in zip(modules, ["adapter", "state_encoder", "behavior"]):
            model.load_state_dict(checkpoint[key])
        predictions = predict(self, *modules, self.test_times)["default"]
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        np.save(output_dir / "test_predictions.npy", predictions, allow_pickle=False)
        (output_dir / "test_node_ids.json").write_text(json.dumps(self.case["unseen_ids"]) + "\n")
        result = scores(self.state[np.ix_(self.unobserved_idxs, self.test_times)], predictions)
        (output_dir / "test_metrics.json").write_text(json.dumps(result, indent=2) + "\n")
        print(f"Test: MAE={result['mae']:.4f}  MAPE={result['mape']:.2f}%  RMSE={result['rmse']:.4f}")
