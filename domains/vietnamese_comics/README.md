# Vietnamese Comics Domain Extension

This extension adapts the general short-video virality pipeline to a concrete startup use case:

> **Vietnamese Comic Short-Video Trend Intelligence**

Primary platforms:
- TikTok
- Facebook Reels

Primary language:
- Vietnamese

Primary business domain:
- comics, manga, manhwa, manhua, webtoon, motion comics, comic reviews, recaps, teasers, character edits, and related entertainment content.

## Business questions

The domain layer should help answer:

1. Which comic-content formats are currently growing?
2. Which hooks and story structures are associated with stronger breakout performance?
3. Which formats work differently on TikTok vs Facebook Reels?
4. Which themes are oversaturated and which are emerging?
5. How similar is a company draft to currently successful content clusters?
6. Which content characteristics are correlated with high share/save/comment behavior?

## Important separation

The **course project core** remains platform-agnostic and compact.

This directory is an extension layer. It should reuse:
- visual embeddings;
- text embeddings;
- audio features;
- normalized virality labels;
- clustering;
- ablation/evaluation.

It adds:
- Vietnamese language-aware features;
- comic-specific content taxonomy;
- hook/story structure features;
- platform-normalized metrics;
- trend momentum;
- company-facing analysis outputs.

## Recommended domain pipeline

```text
TikTok / Facebook Reels
        |
        v
Vietnamese comic niche filtering
        |
        +-----------------------------+
        |                             |
        v                             v
 multimodal features            platform context
 visual/text/audio              platform/time/creator
        |                             |
        +--------------+--------------+
                       v
            normalized breakout score
                       |
          +------------+-------------+
          |                          |
          v                          v
  virality prediction          content clustering
          |                          |
          v                          v
 draft analysis            trend/topic discovery
```

## Recommended data scale

For a real company extension:
- prototype: 1,000–3,000 videos;
- useful niche model: 3,000–10,000 videos;
- stronger trend analysis: 10,000+ videos across repeated time snapshots.

Keep TikTok and Facebook raw metrics separate, then normalize within platform before comparison.

## Suggested first domain experiment

Start with only 6–8 broad content formats:
- story recap;
- review/recommendation;
- motion comic;
- panel slideshow + narration;
- character edit;
- meme/comedy;
- chapter teaser;
- cliffhanger/highlight.

After the embeddings are available, compare these manual labels with unsupervised clusters.
