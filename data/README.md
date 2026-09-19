# Data Layout

Do not commit raw copyrighted video files or private user data unless you have explicit permission to redistribute them.

Recommended files:

```text
data/
├── raw/                 # local/downloaded source data; gitignored
├── interim/
│   └── manifest.csv     # normalized metadata schema
└── processed/
    ├── manifest_labeled.csv
    ├── features.csv
    └── content_embeddings.csv
```

## Minimal manifest schema

| Column | Meaning |
|---|---|
| video_id | stable internal ID |
| creator_id | anonymized/stable creator ID |
| video_path | local path to video |
| posted_at | timestamp |
| caption | caption text |
| hashtags | space-separated or JSON list |
| transcript | ASR transcript |
| duration_sec | video duration |
| followers_at_post | creator followers known at posting time, optional |
| creator_median_views_prev10 | baseline from earlier videos, optional |
| views_7d | target view count at fixed horizon |
| likes_7d | analysis only unless prediction timestamp allows it |
| comments_7d | analysis only unless prediction timestamp allows it |
| shares_7d | analysis only unless prediction timestamp allows it |

`make_labels.py` uses `views_7d` and `creator_median_views_prev10` when both are available.
