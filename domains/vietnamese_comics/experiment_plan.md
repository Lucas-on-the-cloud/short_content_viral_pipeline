# Company Extension Experiment Plan

## Phase A — prove the general pipeline transfers

### A1. Build domain sample
Collect/prepare a permitted dataset of Vietnamese comic short videos.

Target for MVP:
- 1,000–3,000 samples;
- both successful and ordinary/low-performing videos;
- multiple creators;
- bounded time window;
- TikTok first, then Facebook Reels.

### A2. Reuse core baseline
Run:
- metadata baseline;
- visual only;
- text only;
- audio only;
- visual + text;
- all modalities.

### A3. Add domain features
Compare core model vs core +:
- first-3-second hook embedding;
- comic/story features;
- platform indicator.

Key question:
> Does comic-specific modeling improve ranking/prediction beyond generic multimodal embeddings?

---

## Phase B — discover niche content formats

1. Cluster visual + Vietnamese text embeddings.
2. Inspect representative videos.
3. Map clusters to `taxonomy.yaml`.
4. Compare normalized breakout score by cluster.
5. Compare TikTok vs Facebook distributions separately.
6. Track cluster share over time.

Output example:

| Cluster | Working label | TikTok momentum | Facebook momentum | Median breakout |
|---|---|---:|---:|---:|
| C0 | romance cliffhanger | | | |
| C1 | motion comic | | | |
| C2 | review/recommendation | | | |
| C3 | character edit | | | |

---

## Phase C — trend intelligence

Aggregate by week:

- cluster share of uploads;
- median breakout score;
- median share rate;
- number of distinct creators;
- growth in creator adoption;
- growth in video count;
- growth in engagement.

A simple first trend score:

```text
trend_momentum =
0.30 * z(cluster_upload_growth)
+ 0.25 * z(median_breakout_change)
+ 0.20 * z(creator_growth)
+ 0.15 * z(share_rate_change)
+ 0.10 * z(recency)
```

Weights are heuristic at first; validate them later.

---

## Phase D — company draft analyzer

Input:
- draft MP4;
- planned caption;
- planned platform.

Output:
- detected/nearest content format;
- hook characteristics;
- predicted breakout percentile;
- nearest historical examples;
- cluster momentum;
- structural warnings;
- uncertainty/confidence.

Important:
The product should present this as decision support, not a guarantee that a video will go viral.

---

## Suggested sequence

1. **TikTok Vietnamese comics only**
2. add domain taxonomy
3. add hook features
4. validate prediction
5. add clustering
6. add weekly trend momentum
7. only then add Facebook Reels
8. finally build the company-facing analyzer/dashboard

This avoids mixing two platform distributions before the TikTok pipeline is stable.
