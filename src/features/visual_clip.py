"""Frozen CLIP frame embeddings for a single video."""
from __future__ import annotations

import cv2
import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor


def sample_frames(video_path: str, n_frames: int = 8) -> list[Image.Image]:
    cap = cv2.VideoCapture(video_path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total <= 0:
        raise ValueError(f"Cannot read frames from {video_path}")
    indices = np.linspace(0, total - 1, n_frames).astype(int)
    frames = []
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
        ok, frame = cap.read()
        if ok:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame))
    cap.release()
    return frames


@torch.inference_mode()
def encode_video(video_path: str, model_id: str = "openai/clip-vit-base-patch32", n_frames: int = 8) -> np.ndarray:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = CLIPModel.from_pretrained(model_id).to(device).eval()
    processor = CLIPProcessor.from_pretrained(model_id)
    frames = sample_frames(video_path, n_frames)
    batch = processor(images=frames, return_tensors="pt").to(device)
    feats = model.get_image_features(**batch)
    feats = torch.nn.functional.normalize(feats, dim=-1)
    return feats.mean(dim=0).cpu().numpy()
