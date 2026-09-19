# Literature Review

The project should cite a small core of directly relevant work and use the rest as method inspiration.

## Core papers

### 1. Click versus Share: A Feature-driven Study of Micro-Video Popularity and Virality in Social Media — SDM 2018

J. Ding, Y. Li, Y. Li, D. Jin.

- Separates different engagement outcomes rather than treating all popularity signals as equivalent.
- Relevance: motivates careful target definition.
- DOI: https://doi.org/10.1137/1.9781611975321.23

### 2. Understanding Multimodal Popularity Prediction of Social Media Videos With Self-Attention — IEEE Access 2018

A. Bielski, T. Trzcinski.

- Combines temporal self-attention with Grad-CAM-style interpretation.
- Relevance: early work connecting popularity prediction with explanation of content cues.
- DOI: https://doi.org/10.1109/ACCESS.2018.2884831

### 3. A Multimodal Variational Encoder-Decoder Framework for Micro-video Popularity Prediction — WWW 2020

J. Xie et al.

- Models uncertainty in multimodal popularity with variational information bottleneck ideas.
- Uses visual, audio, text and social modalities.
- Code/data: https://github.com/yaochenzhu/MMVED
- ArXiv/full description: https://arxiv.org/abs/2003.12724

### 4. Micro-Video Popularity Prediction Via Multimodal Variational Information Bottleneck — IEEE TMM 2023

J. Xie, Y. Zhu, Z. Chen.

- Extended journal treatment of uncertainty-aware multimodal popularity prediction.
- DOI: https://doi.org/10.1109/TMM.2021.3120537

### 5. Social media popularity prediction with multimodal hierarchical fusion model — Computer Speech & Language 2023

J. Wang, S. Yang, H. Zhao, Y. Yang.

- Hierarchical fusion of visual/text/attribute features.
- Relevance: supports comparing simple concatenation vs structured fusion.
- DOI: https://doi.org/10.1016/j.csl.2023.101490

### 6. AMPS: Predicting Popularity of Short-Form Videos Using Multi-Modal Attention Mechanisms in Social Media Marketing Environments — JRCS 2024

M. Cho, D. Jeong, E. Park.

- Builds a YouTube Shorts dataset.
- Proposes a CDF-based popularity standard.
- Uses multimodal attention.
- Code/data info: https://github.com/dxlabskku/AMPS_short-form-popularity
- DOI: https://doi.org/10.1016/j.jretconser.2024.103778

### 7. Predicting Micro-video Popularity via Multi-modal Retrieval Augmentation — SIGIR 2024

T. Zhong, J. Lang, Y. Zhang, Z. Cheng, K. Zhang, F. Zhou.

- Retrieves similar historical videos and fuses retrieved information with target-video multimodal features.
- Experiments on 19,738 unique MicroLens videos.
- Relevance: strong advanced extension after a basic content model.
- Code: https://github.com/ICDM-UESTC/MMRA
- DOI: https://doi.org/10.1145/3626772.3657929

### 8. Delving Deep into Engagement Prediction of Short Videos — ECCV 2024

D. Li et al.

- Introduces the 90K-video SnapUGC engagement benchmark.
- Uses NAWP and ECR rather than only raw views/likes.
- Evaluates multimodal content features.
- Code/data: https://github.com/dasongli1/snapugc_engagement

### 9. Multi-Modal Video Feature Extraction for Popularity Prediction — 2025

H. Liu et al.

- Compares video transformers/VLMs for feature extraction.
- Combines neural video/text predictions with engineered tabular features and XGBoost.
- Relevance: very close to the proposed lightweight course architecture.
- ArXiv: https://arxiv.org/abs/2501.01422

### 10. Large Language Models Are Natural Video Popularity Predictors — Findings of ACL 2025

P. Kayal, P. Mettes, N. Dehmamy, M. Park.

- Converts frame-level visuals to text with vision-language models and uses LLM reasoning/context for popularity prediction.
- Evaluates on 13,639 popular videos.
- Relevance: optional VLM/LLM extension and evidence that semantic context matters.
- Paper: https://aclanthology.org/2025.findings-acl.597/

### 11. Engagement Prediction of Short Videos with Large Multimodal Models — ICCV Workshops 2025

W. Sun et al.

- Tests VideoLLaMA2 and Qwen2.5-VL on SnapUGC.
- Reports that adding audio with VideoLLaMA2 is useful in their setup.
- Relevance: supports keeping audio as a meaningful modality, but the models are too heavy for the default course baseline.
- Code: https://github.com/sunwei925/LMM-EVQA

### 12. Short-video Propagation Influence Rating: A New Real-world Dataset and a New Large Graph Model — IEEE TKDE 2026

D. Xue, S. Qian, C. Hu, C. Xu.

- Introduces XS-Video and a graph + multimodal LLM approach.
- Relevance: demonstrates the importance of social propagation context beyond content.
- Code/data: https://github.com/LivXue/short-video-influence

### 13. Will It Go Viral? Grounding Micro-Video Popularity Prediction on the Open Web — 2026

R. Heo, D. Lee.

- Introduces WEBSHORTS (14K videos), seven-day view tracking and real-time web context.
- Relevance: explicitly highlights trend/context shift, a limitation of content-only models.
- ArXiv: https://arxiv.org/abs/2605.18653

### 14. Tell popular from unpopular: A popularity-guided bipolar multimodal interactive prototype learning method for micro-video popularity prediction — Expert Systems with Applications 2026

T. Cheng et al.

- Separates popularity-supportive and popularity-suppressive signals with contrastive/prototype learning and hierarchical attention.
- Relevance: interesting interpretability/fusion reference, but beyond the default course implementation.
- DOI: https://doi.org/10.1016/j.eswa.2026.131802

---

## Recommended reading order

1. SnapUGC (problem + modern benchmark)
2. AMPS (short-form labels + attention)
3. MMRA (retrieval augmentation)
4. Multi-Modal Video Feature Extraction 2025 (practical feature pipeline)
5. Bielski & Trzcinski 2018 (interpretability)
6. LLM popularity paper 2025 (semantic/VLM extension)
7. WEBSHORTS 2026 (trend/context limitation)

For a course project, implementing ideas from #1, #2, #4 and #5 is enough. The rest belongs in related work/future work.
