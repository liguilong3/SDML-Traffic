import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
from pathlib import Path
import argparse
from datetime import datetime
from sdml.data import ROOT, load_experiment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT / "configs/flow15.json")
    parser.add_argument("--mode", choices=["train", "infer"], default="train")
    parser.add_argument("--seed", type=int, help="Optional training-seed override.")
    parser.add_argument("--device", choices=["cpu", "cuda", "auto"], default=None)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--check-data", action="store_true")
    parser.add_argument("--smoke", action="store_true", help="Two training batches; not the full experiment.")
    args = parser.parse_args()
    document, states, embeddings = load_experiment(args.config)
    if args.seed is not None:
        if not 0 <= args.seed < 2**32:
            parser.error("--seed must be an unsigned 32-bit integer.")
        document["training"]["training_seed"] = args.seed
    cfg = document["training"]
    output = args.output_dir or ROOT / "outputs" / (
        f"flow15_seed{cfg['training_seed']}_" + datetime.now().strftime("%Y%m%d_%H%M%S_%f"))
    if args.check_data:
        print(f"{document['case']['name']}: states={states.shape}, embeddings={embeddings.shape}, "
              f"seen={len(document['case']['seen_indices'])}, unseen={len(document['case']['unseen_indices'])}, "
              f"seed={cfg['training_seed']}, epochs={cfg['epochs']}")
        return
    from sdml.experiment import Experiment
    experiment = Experiment(document, states, embeddings,
                            device=args.device or document.get("device", "cpu"), smoke=args.smoke)
    if args.mode == "infer":
        if args.checkpoint is None or args.smoke:
            parser.error("Inference requires --checkpoint and does not accept --smoke.")
        experiment.infer(args.checkpoint, output)
    else:
        experiment.train(output)
    print(f"Outputs: {output.resolve()}")


if __name__ == "__main__":
    main()
