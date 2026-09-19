# Candidate Datasets

## Recommendation for this course project

Use one of two routes:

### Route A — niche-specific TikTok data

Best match to the original idea, but only if collection is permitted and technically reliable.

Recommended design:
- one niche;
- 2,000–10,000 videos;
- collect posts from a bounded time window;
- record creator context at collection/posting time where possible;
- use a fixed prediction horizon such as 7 days;
- recrawl/re-measure after the horizon if the data source permits;
- compute a creator-normalized breakout target.

This avoids comparing a brand-new video to an old video that has had months to accumulate views.

### Route B — public research dataset

Safer and faster for a class project. Reproduce an academic benchmark first, then add content-pattern discovery.

---

## 1. TikTok Trending December 2020

- Platform: TikTok
- Size: 1,000 trending videos
- Includes: video files and engagement metadata
- Strength: extremely easy baseline/reproduction dataset
- Weakness: almost entirely trending/popular content; weak negative class and old distribution
- Link: https://www.kaggle.com/datasets/erikvdven/tiktok-trending-december-2020
- Example codebases:
  - https://github.com/harbarex/tiktok-virality-prediction
  - https://github.com/casparbreloh/virality-prediction

**Use:** sanity check / reproduction, not the strongest final dataset.

## 2. SnapUGC Engagement

- Platform: Snapchat short-form UGC
- Size: 90,000 videos
- Labels: normalized average watch percentage (NAWP) and engagement continuation rate (ECR)
- Modalities: visual, background music, text
- Paper: *Delving Deep into Engagement Prediction of Short Videos*, ECCV 2024
- Repo: https://github.com/dasongli1/snapugc_engagement

**Use:** strongest practical public benchmark for content-based engagement prediction. Subsample 5k–15k if compute is limited.

## 3. MicroLens / MMRA subset

- Platform type: micro-video platforms
- MMRA experiments: 19,738 unique micro-videos from a larger MicroLens collection
- Modalities: visual + text and retrieval context
- Paper: *Predicting Micro-video Popularity via Multi-modal Retrieval Augmentation*, SIGIR 2024
- Repo: https://github.com/ICDM-UESTC/MMRA
- Original MicroLens: https://github.com/westlake-repl/MicroLens

**Use:** good if you want a research-oriented popularity benchmark and retrieval-based extension.

## 4. Xigua / NUS from MMVED

- Xigua contains temporal popularity labels plus visual/audio/text/social features.
- NUS is used for micro-video popularity regression.
- Paper: *A Multimodal Variational Encoder-Decoder Framework for Micro-video Popularity Prediction*, WWW 2020
- Repo/data: https://github.com/yaochenzhu/MMVED

**Use:** very convenient for model benchmarking because extracted features are already available; less suitable for discovering rich new content formats from raw video.

## 5. AMPS Short-Form Popularity Dataset

- Platform: YouTube Shorts
- Data: short-form video/content and channel metadata
- Method: CDF-based popularity standard + multimodal attention
- Paper: Cho, Jeong & Park, *AMPS: Predicting popularity of short-form videos using multi-modal attention mechanisms in social media marketing environments*, Journal of Retailing and Consumer Services, 2024
- Repo: https://github.com/dxlabskku/AMPS_short-form-popularity

**Use:** very close conceptual match, especially for popularity-label design.

## 6. Tsinghua Large-Scale Mobile Short-Video Dataset

- Paper: *A Large-scale Dataset with Behavior, Attributes, and Content of Mobile Short-video Platform*, Web Conference Companion 2025
- Provides behavior, attributes, content and feature-processing code
- Repo: https://github.com/tsinghua-fib-lab/ShortVideo_dataset

**Use:** interesting for large-scale recommendation/behavior research; likely more data engineering than needed for a course project.

## 7. XS-Video

- Paper/task: short-video propagation influence rating, TKDE 2026
- Size reported by the authors: 117,720 videos, 381,926 samples, 535 topics across five Chinese platforms
- Includes social propagation / engagement context
- Repo: https://github.com/LivXue/short-video-influence

**Use:** advanced reference only. The authors' model requires a much heavier graph + multimodal stack than this course project needs.

## 8. WEBSHORTS

- Paper: *Will It Go Viral? Grounding Micro-Video Popularity Prediction on the Open Web*, 2026
- Size: 14K videos
- Tracks daily views over 7 days and adds web-context evidence captured near upload time
- ArXiv: https://arxiv.org/abs/2605.18653

**Use:** conceptually excellent for understanding why content-only prediction has limits. Treat as an advanced/future extension unless code/data access is convenient.

---

## Dataset decision matrix

| Dataset | Raw short video | Engagement label | Easy to use | Match to TikTok idea | Recommended role |
|---|---:|---:|---:|---:|---|
| TikTok Trending 2020 | ✓ | ✓ | ✓✓✓ | ✓✓✓ | reproduction only |
| SnapUGC | ✓ | ✓✓✓ | ✓✓ | ✓✓ | primary public benchmark |
| MicroLens/MMRA | ✓/features | ✓✓ | ✓✓ | ✓✓ | research benchmark |
| Xigua/NUS | features | ✓✓ | ✓✓✓ | ✓✓ | fast modeling baseline |
| AMPS | dataset access via authors | ✓✓ | ✓✓ | ✓✓ | label/method reference |
| Tsinghua ShortVideo | mixed | behavior-heavy | ✓ | ✓✓ | large-scale extension |
| XS-Video | ✓/graph | ✓✓✓ | difficult | ✓✓ | advanced reference |
| WEBSHORTS | ✓ | fixed-horizon views | TBD | ✓✓ | future/trend-context extension |
