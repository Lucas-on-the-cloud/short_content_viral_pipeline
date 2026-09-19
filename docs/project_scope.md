# Project Scope

## Working title

**Short-Form Video Virality Prediction and Content Pattern Discovery**

## Goal

Build a compact multimodal machine-learning system that predicts normalized short-video popularity and discovers recurring content formats associated with stronger engagement inside one niche.

## What is in scope

- one short-video niche;
- 2k–10k samples where practical;
- video, caption/transcript, audio and simple creator/context features;
- frozen pretrained feature extractors;
- regression + binary classification;
- creator-grouped validation;
- ablation study;
- unsupervised content clustering;
- interpretable feature analysis.

## What is explicitly out of scope

- reconstructing TikTok's recommender system;
- claiming causal rules for virality;
- training a large video transformer or multimodal LLM from scratch;
- social-network propagation graphs unless an existing dataset already provides them;
- real-time production deployment.

## Minimum viable project

1. Obtain a public dataset or a class-approved collection of at least ~2,000 short videos.
2. Create leakage-safe labels.
3. Train one metadata baseline.
4. Extract frozen visual and text embeddings.
5. Train one multimodal model.
6. Compare modalities with ablation.
7. Cluster content embeddings and summarize which clusters show higher/lower normalized engagement.

## Strong final-project version

Add audio, SHAP, HDBSCAN, temporal split, creator-normalized labels, and a small demo that accepts one video and returns a predicted percentile plus nearest content cluster.
