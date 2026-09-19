"""Small late-fusion regressor for precomputed modality embeddings."""
from __future__ import annotations

import torch
from torch import nn


class FusionMLP(nn.Module):
    def __init__(self, visual_dim: int, text_dim: int, audio_dim: int, hidden: int = 128):
        super().__init__()
        self.visual = nn.Sequential(nn.Linear(visual_dim, hidden), nn.ReLU(), nn.Dropout(0.2))
        self.text = nn.Sequential(nn.Linear(text_dim, hidden), nn.ReLU(), nn.Dropout(0.2))
        self.audio = nn.Sequential(nn.Linear(audio_dim, hidden), nn.ReLU(), nn.Dropout(0.2))
        self.head = nn.Sequential(
            nn.Linear(hidden * 3, hidden),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden, 1),
        )

    def forward(self, visual: torch.Tensor, text: torch.Tensor, audio: torch.Tensor) -> torch.Tensor:
        z = torch.cat([self.visual(visual), self.text(text), self.audio(audio)], dim=-1)
        return self.head(z).squeeze(-1)
