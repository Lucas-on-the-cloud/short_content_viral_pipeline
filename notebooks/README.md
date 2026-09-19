# Notebook Plan

Recommended Kaggle notebooks:

1. `01_eda.ipynb` — inspect labels, creators, time window, missing data.
2. `02_feature_extraction.ipynb` — CLIP/text/audio embeddings; save processed CSV/Parquet.
3. `03_baselines.ipynb` — grouped split + metadata/single-modality baselines.
4. `04_multimodal_ablation.ipynb` — fusion and ablation table.
5. `05_content_clusters.ipynb` — PCA/UMAP, K-Means/HDBSCAN, cluster interpretation.
6. `06_final_demo.ipynb` — one-video inference demo.

Keep feature extraction separate from model training so expensive embeddings are cached once.
