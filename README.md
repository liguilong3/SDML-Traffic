# SDML: Zero-Shot Urban Traffic State Inference

Code and materials for Semantically-guided Dynamic Metric Learning (SDML): the model, Torino traffic-flow data, KG embeddings, LLM-augmented knowledge graphs, and the LLM prompts.

## Structure

```text
├── run.py                  # Entry point (training and inference)
├── requirements.txt
├── configs/flow15.json     # Default node split, training seed, and hyperparameters
├── sdml/                   # Model, data loading, training, evaluation
├── data/flow/              # Torino traffic-flow observations and detector info
├── embeddings/             # KG embeddings for Flow and Parking
├── knowledge_graphs/       # Augmented knowledge graphs and schema
└── prompts/
    ├── kg_augmentation/    # KG augmentation templates, one example each
    └── llm_baselines/      # LLM baseline templates, one example each
```

## Run

Python 3.9 or newer.

```bash
python -m pip install -r requirements.txt
python run.py
```

Inference on the unobserved nodes, using the model saved by the run above:

```bash
python run.py --mode infer --checkpoint outputs/<run>/model.pt
```

## Citation

If you use this code, please cite our paper. The citation will be provided here once the paper is available.

## Data

The Torino traffic-flow data in `data/flow/` are a processed subset of [UTD19](https://utd19.ethz.ch/) and are provided for academic and non-commercial use only. If you use these data, please also cite the original dataset:

> Loder, A., Ambühl, L., Menendez, M., & Axhausen, K. W. (2019). Understanding traffic capacity of urban networks. *Scientific Reports*, 9. https://doi.org/10.1038/s41598-019-51539-5

and acknowledge the data source as "UTD19 (utd19.ethz.ch)".
