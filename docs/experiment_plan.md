# Experiment Plan

## Experiment 0 — data sanity

- plot label distribution;
- inspect creator frequency;
- inspect video age / time-window distribution;
- check missing modalities;
- check duplicates/reposts;
- verify there are no post-outcome engagement features in model inputs.

## Experiment 1 — naive + metadata baseline

Models:
- mean/median predictor;
- HistGradientBoosting;
- XGBoost if available.

Goal: establish whether creator/context/structural features already explain a large fraction of performance.

## Experiment 2 — single modalities

Train on:
- visual embedding only;
- text embedding only;
- audio features only.

This is more informative than immediately training one giant fused model.

## Experiment 3 — multimodal fusion

Compare:
- concatenation + XGBoost;
- concatenation + small MLP;
- optional gated fusion MLP.

## Experiment 4 — content clusters

Use only content embeddings.

Compare K-Means solutions for 5–12 clusters. Pick a stable interpretable configuration, not simply the one that maximizes association with the target.

For each cluster report:
- size;
- representative videos/captions;
- top keywords;
- median breakout score;
- IQR;
- viral-class proportion.

## Experiment 5 — explanation

- SHAP for metadata/structural model;
- modality ablation for multimodal model;
- optional nearest-neighbor examples for each prediction.

## Suggested final result tables

### Table A — predictive performance

| Model | MAE ↓ | RMSE ↓ | Spearman ↑ | R² ↑ |
|---|---:|---:|---:|---:|
| Naive | | | | |
| Metadata | | | | |
| Visual | | | | |
| Text | | | | |
| Audio | | | | |
| Visual + Text | | | | |
| All content | | | | |
| All content + context | | | | |

### Table B — ablation

| Removed modality | ΔMAE | ΔSpearman |
|---|---:|---:|
| visual | | |
| text | | |
| audio | | |
| creator/context | | |

### Table C — discovered content formats

| Cluster | Working label | N | Median breakout | Viral % | Example pattern |
|---|---|---:|---:|---:|---|
| C0 | | | | | |
| C1 | | | | | |
| ... | | | | | |

## Final demo

Input: one short video + caption.

Output:
- predicted breakout score / percentile;
- predicted viral class;
- nearest content cluster;
- nearest historical examples (optional);
- top structural/context contributors from the tabular model.
