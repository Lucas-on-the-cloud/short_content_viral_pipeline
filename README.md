# Short-Form Video Virality Prediction & Content Pattern Discovery

Course final project for predicting short-video popularity from **content available at or before upload** and discovering recurring content patterns associated with stronger engagement.

> Scope: one content niche, a few thousand short videos, frozen pretrained feature extractors, lightweight prediction models, and interpretable analysis. This is intentionally smaller than a capstone/research-paper-scale project.

## 1. Project idea

Given a short video, caption, hashtags, audio, and creator context, estimate its **normalized virality** and analyze which recurring content formats are associated with stronger performance.

The project has two outputs:

1. **Virality prediction** — regression and/or top-20% viral classification.
2. **Content pattern discovery** — cluster videos by multimodal content embeddings, then compare the engagement distribution of the discovered clusters.

This is not an attempt to reverse-engineer TikTok's recommendation algorithm. The goal is to model associations between observable content/context and later engagement.

## 2. Research questions

- **RQ1:** How well can short-video virality be predicted from pre-publication multimodal features?
- **RQ2:** Does multimodal fusion outperform metadata-only, visual-only, text-only, and audio-only baselines?
- **RQ3:** Which content clusters/formats are associated with higher normalized virality within one niche?
- **RQ4:** Which features/modalities contribute most to the prediction?

## 3. Recommended dataset scope

For a course project, target **2,000–10,000 videos from one niche**. Examples: skincare, café reviews, study content, fitness, gaming clips, or language learning.

If TikTok collection is not practical or permitted, use a public short-video benchmark such as SnapUGC, MicroLens, AMPS/YouTube Shorts, Xigua/NUS, or the TikTok Trending December 2020 dataset for a reproduction baseline.

Important: the old 1,000-video TikTok trending dataset contains only trending videos, so it is useful for reproduction but weak for learning the difference between viral and non-viral content.

## 4. Label design

Avoid predicting raw views alone because creator size strongly affects view count.

Recommended regression target:

```text
breakout_score = log1p(views_7d) - log1p(creator_median_views_prev10)
```

Recommended classification target:

```text
viral = 1 if breakout_score is in the top 20% of the training set
        0 otherwise
```

Alternative: use the empirical CDF/percentile of engagement within the same niche/time window, inspired by AMPS.

Do **not** use likes, comments, shares, or view counts observed after publication as input features when the task is supposed to predict performance before publication. That would be target leakage.

## 5. Default pipeline

```text
Video + Caption + Hashtags + Creator Context
                  |
      +-----------+------------+
      |           |            |
    Visual       Text         Audio
  CLIP frames  transcript    MFCC / AST
      |           |            |
      +------ frozen embeddings+
                  |
       handcrafted structure
 duration / cuts / text length / posting time
                  |
        feature-level baseline
          XGBoost / MLP
                  |
      normalized virality score

Content-only embeddings
        |
   PCA / UMAP
        |
 K-Means / HDBSCAN
        |
content-format clusters
        |
cluster virality analysis
```

## 6. Models to compare

### Baseline A — metadata / handcrafted features

- duration
- caption length
- hashtag count
- posting hour/day
- creator follower count at posting time (if available)
- creator historical median views (if available)
- scene-cut count
- speech/text density

Model: **XGBoost** or HistGradientBoosting.

### Baseline B — content embeddings

- visual: CLIP over 8 uniformly sampled frames, mean-pooled
- text: multilingual Sentence Transformer over caption + transcript
- audio: MFCC summary vector (simple) or an audio foundation-model embedding (advanced)

Model: concatenated embeddings + XGBoost / small MLP.

### Model C — lightweight multimodal fusion

Separate projection layers for visual/text/audio, followed by concatenation or gated/late fusion and a small MLP prediction head.

For this course project, do **not** train TimeSformer, ViViT, VideoMAE, VideoLLaMA, or Qwen-VL from scratch. They are literature references / optional extensions.

## 7. Content-pattern discovery

Clustering must use **content features only**, not engagement labels.

Suggested procedure:

1. concatenate visual + text embeddings;
2. reduce dimension with PCA (and UMAP for visualization only);
3. cluster with K-Means first; optionally compare HDBSCAN;
4. inspect representative videos/captions from each cluster;
5. name clusters manually using observable format, e.g. `before-after`, `tutorial`, `storytime`, `product-review`, `trend-remix`;
6. compare breakout-score distributions between clusters;
7. report median, IQR, confidence interval and a non-parametric test such as Kruskal-Wallis.

Interpret cluster results as **association**, not proof that a format causes virality.

## 8. Evaluation

Use a **creator-grouped split** so videos from the same creator do not appear in both training and test sets.

Regression:
- MAE
- RMSE
- Spearman correlation
- R²

Classification:
- F1
- ROC-AUC
- PR-AUC

Ablation table:

| Experiment | Visual | Text | Audio | Metadata |
|---|---:|---:|---:|---:|
| Metadata baseline |  |  |  | ✓ |
| Visual only | ✓ |  |  |  |
| Text only |  | ✓ |  |  |
| Audio only |  |  | ✓ |  |
| Content multimodal | ✓ | ✓ | ✓ |  |
| Full model | ✓ | ✓ | ✓ | ✓ |

## 9. Repository structure

```text
.
├── configs/
│   └── base.yaml
├── data/
│   ├── README.md
│   ├── raw/
│   ├── interim/
│   └── processed/
├── docs/
│   ├── datasets.md
│   ├── experiment_plan.md
│   ├── literature_review.md
│   ├── methodology.md
│   └── project_scope.md
├── notebooks/
│   └── README.md
├── src/
│   ├── features/
│   │   ├── audio_mfcc.py
│   │   ├── text_embedding.py
│   │   └── visual_clip.py
│   ├── models/
│   │   └── fusion_mlp.py
│   ├── cluster_content.py
│   ├── make_labels.py
│   └── train_baseline.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 10. Suggested 8-week plan

| Week | Deliverable |
|---|---|
| 1 | finalize niche, label definition, dataset source |
| 2 | data collection / download + EDA |
| 3 | data cleaning + leakage-safe creator split |
| 4 | metadata baseline + first metrics |
| 5 | extract visual/text/audio features |
| 6 | multimodal prediction + ablation |
| 7 | clustering + SHAP + content-pattern analysis |
| 8 | final report, slides, demo notebook |

## 11. Quick start

```bash
pip install -r requirements.txt
python src/make_labels.py --input data/interim/manifest.csv --output data/processed/manifest_labeled.csv
python src/train_baseline.py --input data/processed/features.csv --target breakout_score --group creator_id
python src/cluster_content.py --input data/processed/content_embeddings.csv --target breakout_score
```

See `docs/` for the research plan, papers, datasets, and experiment design.


## 12. Vietnamese comics startup extension

The repository also contains an optional business/domain adaptation layer for a Vietnamese comics startup:

```text
domains/vietnamese_comics/
├── README.md
├── config.yaml
├── data_schema.md
├── experiment_plan.md
├── feature_spec.md
└── taxonomy.yaml
```

This extension focuses on:
- TikTok first, then Facebook Reels;
- Vietnamese-language short-form content;
- comics / manga / manhwa / manhua / webtoon;
- hook analysis in the first ~3 seconds;
- story/narrative structure;
- comic-specific visual features;
- platform-normalized breakout scores;
- weekly content-cluster trend momentum;
- a future company-facing draft analyzer.

The **course project core stays unchanged and platform-agnostic**. The Vietnamese comics layer reuses the same multimodal embeddings, normalized labels, clustering, and evaluation pipeline, then adds domain-specific features and business outputs.

See [domains/vietnamese_comics/README.md](domains/vietnamese_comics/README.md) for the extension design.
