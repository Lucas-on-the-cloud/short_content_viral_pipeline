# Vietnamese Comic Dataset Schema

Use one row per video observation.

## Identity

| Column | Type | Description |
|---|---|---|
| video_id | string | internal stable identifier |
| platform | category | `tiktok` or `facebook_reels` |
| creator_id | string | stable/anonymized creator identifier |
| collected_at | datetime | when this snapshot was collected |
| posted_at | datetime | publication time |
| source_url_hash | string | optional hash, not necessarily the raw URL |

## Content

| Column | Type | Description |
|---|---|---|
| caption | text | original caption |
| hashtags | text/list | original hashtags |
| transcript_vi | text | Vietnamese ASR transcript |
| ocr_text_vi | text | OCR text from keyframes |
| duration_sec | float | video duration |
| content_format | category | optional manual/weak label from taxonomy |
| story_genre | category | optional |
| hook_type | category | optional |
| hook_text | text | text/speech from first ~3 seconds |

## Creator context known before posting

| Column | Type | Description |
|---|---|---|
| followers_at_post | int | if available and permitted |
| creator_median_views_prev10 | float | creator baseline from earlier posts |
| creator_median_engagement_prev10 | float | optional |

## Fixed-horizon outcomes

Keep outcome horizons explicit.

| Column | Type |
|---|---|
| views_24h | int |
| views_7d | int |
| likes_7d | int |
| comments_7d | int |
| shares_7d | int |
| saves_7d | int, if available |

Never feed these post-publication outcomes into a model that claims to predict performance before publication.

## Platform-normalized labels

Recommended derived columns:

```text
breakout_score
platform_percentile_7d
niche_percentile_7d
viral_label
share_rate_7d
comment_rate_7d
```

Example:

```text
platform_percentile_7d =
percentile_rank(breakout_score within platform + collection window)
```

This makes TikTok and Facebook performance comparable without assuming equal raw view distributions.

## Time snapshots for trend discovery

For trend analysis, store repeated observations rather than only a final count:

```text
video_id
snapshot_time
views
likes
comments
shares
```

This allows growth-velocity and trend-momentum features.
