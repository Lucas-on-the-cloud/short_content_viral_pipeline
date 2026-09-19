# Methodology

## 1. Problem definition

For each video `i`, predict later popularity from information that exists at posting time.

A robust creator-normalized target is:

```text
breakout_i = log(1 + views_i,7d) - log(1 + median(previous 10 views of creator_i))
```

If creator history is unavailable, use a niche/time-window percentile target rather than raw view count.

## 2. Data leakage rules

Features allowed for a pre-publication task:

- pixels / frames;
- audio;
- spoken transcript;
- on-screen text;
- caption and hashtags;
- video duration and editing structure;
- creator statistics known before publication;
- planned posting time;
- sound/trend statistics known at posting time, if available.

Features not allowed:

- final view count;
- later likes, comments or shares;
- watch-time accumulated after posting;
- any engagement metric measured after the prediction timestamp.

## 3. Split strategy

Default: `GroupShuffleSplit` by `creator_id`.

Why: a random video-level split lets the model memorize creator identity/style, often making results look better than real generalization.

Advanced: additionally use a chronological split to evaluate distribution shift.

## 4. Feature extraction

### Visual

Default:
- uniformly sample 8 frames;
- encode each frame with CLIP ViT-B/32;
- L2-normalize and mean-pool.

Possible extension:
- VideoMAE / TimeSformer / ViViT embeddings.

### Text

Concatenate:

```text
caption [SEP] hashtags [SEP] transcript
```

Encode with a multilingual Sentence Transformer. For English-only data, a compact English model is sufficient.

Optional:
- OCR from keyframes;
- hook text from first 3 seconds separately from the full transcript.

### Audio

Course-project default:
- MFCC mean/std;
- spectral centroid;
- tempo;
- zero-crossing rate.

Advanced:
- AST, PANNs, YAMNet or another pretrained audio model.

### Structural features

- duration;
- number of scene cuts;
- cuts per second;
- transcript word count;
- speech rate;
- caption length;
- hashtag count;
- face/object counts if easy to extract.

## 5. Predictive models

### M0: naive baseline

Predict train-set mean/median breakout score.

### M1: metadata baseline

XGBoost / HistGradientBoosting over tabular and structural features.

### M2: single-modality baselines

- visual only;
- text only;
- audio only.

### M3: early feature fusion

Concatenate standardized modality embeddings and fit XGBoost or an MLP.

### M4: lightweight late/gated fusion (optional)

Project modalities separately, learn modality weights, fuse, then predict.

## 6. Content-pattern discovery

Use visual + text content embeddings only.

1. Standardize.
2. PCA to 32–128 dimensions.
3. K-Means with `k=5..12`; choose a stable interpretable solution.
4. Optional HDBSCAN comparison.
5. UMAP only for 2-D plotting, not as evidence by itself.
6. Inspect cluster exemplars and top textual terms.
7. Assign human-readable names.
8. Compare `breakout_score` distributions across clusters.

This answers "what content formats are associated with virality?" without letting engagement labels define the clusters.

## 7. Explainability

For XGBoost/tabular models:
- SHAP summary plot;
- permutation importance.

For embedding dimensions, raw SHAP is less interpretable. Prefer modality-level ablation and structural/metadata feature SHAP.

## 8. Statistics

Virality metrics are usually skewed, so report median/IQR in addition to mean.

For cluster comparisons:
- Kruskal-Wallis across all clusters;
- post-hoc pairwise tests only if needed;
- bootstrap confidence intervals for cluster median breakout score.

## 9. Evaluation

Regression:
- MAE;
- RMSE;
- Spearman rho;
- R².

Classification:
- F1;
- ROC-AUC;
- PR-AUC.

Never select the test set threshold using test labels. Fit all preprocessing and viral-percentile thresholds using training data only.
