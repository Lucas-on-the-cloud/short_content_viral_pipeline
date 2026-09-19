"""Sentence-transformer text embedding."""
from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer


def encode_text(
    caption: str = "",
    hashtags: str = "",
    transcript: str = "",
    model_id: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
) -> np.ndarray:
    model = SentenceTransformer(model_id)
    text = f"{caption} [SEP] {hashtags} [SEP] {transcript}".strip()
    emb = model.encode(text, normalize_embeddings=True)
    return np.asarray(emb, dtype=np.float32)
