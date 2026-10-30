import numpy as np
import torch
import faiss

def scores(truth, predictions):
    errors = truth.astype(np.float64) - predictions.astype(np.float64)
    return dict(mae=float(np.abs(errors).mean()),
                rmse=float(np.sqrt(np.square(errors).mean())),
                mape=float((np.abs(errors / (truth.astype(np.float64) + 1e-8))).mean()*100))

@torch.no_grad()
def predict(runner, adapter, encoder, behavior, times, counts=None, batch_size=64):
    for model in (adapter, encoder, behavior):
        model.eval()
    counts = counts or {'default': runner.TOP_K}
    counts = {label: min(int(k), runner.N_obs) for label, k in counts.items()}
    result = {label: np.empty((runner.N_unobs, len(times)), dtype=np.float64) for label in counts}
    semantic = adapter(torch.arange(runner.N, device=runner.DEVICE))
    for start in range(0, len(times), batch_size):
        current = np.asarray(times[start:start+batch_size])
        indices = current[:, None] - runner.W + 1 + np.arange(runner.W)[None, :]
        values = runner.state_norm_obs[:, indices].transpose(1, 2, 0)
        context = np.stack([values, np.ones_like(values)], axis=1).astype(np.float32)
        h = encoder(torch.from_numpy(context).to(runner.DEVICE))
        size = len(current)
        b = behavior(semantic.unsqueeze(0).expand(size, -1, -1).reshape(-1, semantic.shape[-1]),
                     h[:, None, :].expand(-1, runner.N, -1).reshape(-1, h.shape[-1]))
        b = b.reshape(size, runner.N, runner.BEHAVIOR_DIM).cpu().numpy()
        for offset, time in enumerate(current):
            index = faiss.IndexFlatIP(runner.BEHAVIOR_DIM)
            index.add(np.ascontiguousarray(b[offset, runner.observed_idxs]))
            query = np.ascontiguousarray(b[offset])
            probe, _ = index.search(query, min(max(counts.values()) + 1, runner.N_obs))
            boundary_tie = any(count < runner.N_obs and np.any(
                probe[runner.unobserved_idxs, count-1] - probe[runner.unobserved_idxs, count] < 2e-6)
                for count in counts.values())
            if boundary_tie:
                single = torch.from_numpy(context[offset:offset+1]).to(runner.DEVICE)
                single_h = encoder(single).repeat(runner.N, 1)
                query = behavior(semantic, single_h).cpu().numpy()
                index = faiss.IndexFlatIP(runner.BEHAVIOR_DIM)
                index.add(np.ascontiguousarray(query[runner.observed_idxs]))
            for label, count in counts.items():
                similarities, neighbors = index.search(query, count)
                similarities = similarities[runner.unobserved_idxs]
                neighbors = neighbors[runner.unobserved_idxs]
                weights = np.exp(similarities.astype(np.float64) / runner.TEMPERATURE)
                weights /= weights.sum(axis=1, keepdims=True) + 1e-9
                nodes = runner.observed_idxs[neighbors]
                result[label][:, start+offset] = (weights * runner.state_norm[nodes, time]).sum(axis=1) * runner.STATE_VALUE_SCALE
    return result
