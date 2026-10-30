from pathlib import Path
import csv
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def load_experiment(config_path):
    document = json.loads(Path(config_path).read_text(encoding="utf-8"))
    case, cfg, files = document["case"], document["training"], document["files"]
    with (ROOT / files["info"]).open(encoding="utf-8-sig", newline="") as handle:
        ids = [row["detid"] for row in csv.DictReader(handle)]
    embedding_ids = json.loads((ROOT / files["embedding_node_ids"]).read_text())
    if ids != list(map(str, embedding_ids)) or len(set(ids)) != len(ids):
        raise ValueError("Observation rows and KG embedding node IDs must match exactly.")
    seen, unseen = case["seen_indices"], case["unseen_indices"]
    if sorted(seen + unseen) != list(range(len(ids))):
        raise ValueError("Seen and unseen indices must partition all nodes exactly once.")
    for indices, label in [(seen, "seen"), (unseen, "unseen")]:
        if [ids[i] for i in indices] != list(map(str, case[label + "_ids"])):
            raise ValueError("The fixed node IDs do not match their row indices.")
    states = np.load(ROOT / files["states"], allow_pickle=False).astype(np.float32)
    embeddings = np.load(ROOT / files["embedding"], allow_pickle=False).astype(np.float32)
    if states.ndim != 2 or states.shape[0] != len(ids):
        raise ValueError("Observation rows do not match the node IDs.")
    if embeddings.ndim != 2 or embeddings.shape[0] != len(ids):
        raise ValueError("KG embedding rows do not match the node IDs.")
    if not np.isfinite(states).all() or not np.isfinite(embeddings).all():
        raise ValueError("Inputs must be finite.")
    if np.any(np.all(embeddings == 0, axis=1)):
        raise ValueError("An all-zero KG embedding row was supplied.")
    if not (1 <= cfg["top_k"] <= len(seen) and
            1 <= cfg["top_k_positive"] < len(seen)):
        raise ValueError("Invalid inference or positive-pool neighbor count.")
    end = int(states.shape[1] * cfg["train_fraction"])
    if not cfg["window"] < end < states.shape[1]:
        raise ValueError("Invalid training/test boundary.")
    return document, states, embeddings
