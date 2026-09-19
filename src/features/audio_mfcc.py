"""Lightweight audio descriptors for a course-project baseline."""
from __future__ import annotations

import numpy as np
import librosa


def encode_audio(path: str, sr: int = 22050, n_mfcc: int = 20) -> np.ndarray:
    y, sr = librosa.load(path, sr=sr, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return np.concatenate([
        mfcc.mean(axis=1),
        mfcc.std(axis=1),
        [float(centroid.mean()), float(centroid.std()), float(zcr.mean()), float(np.asarray(tempo).squeeze())],
    ]).astype(np.float32)
