"""Cluster content-only embeddings and summarize virality by cluster."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--target", default="breakout_score")
    p.add_argument("--k", type=int, default=8)
    p.add_argument("--output", default="outputs/clustered_content.csv")
    args = p.parse_args()

    df = pd.read_csv(args.input)
    emb_cols = [c for c in df.columns if c.startswith(("visual_", "text_", "audio_"))]
    if not emb_cols:
        raise ValueError("Expected embedding columns beginning visual_, text_, or audio_.")

    X = StandardScaler().fit_transform(df[emb_cols].fillna(0))
    pca_dim = min(64, X.shape[1], max(2, X.shape[0] - 1))
    Z = PCA(n_components=pca_dim, random_state=42).fit_transform(X)
    labels = KMeans(n_clusters=args.k, n_init="auto", random_state=42).fit_predict(Z)

    out = df.copy()
    out["content_cluster"] = labels
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(path, index=False)

    if args.target in out.columns:
        summary = out.groupby("content_cluster")[args.target].agg(["count", "median", "mean", "std"])
        print(summary.to_string())
    print(f"Wrote clustered dataset -> {path}")


if __name__ == "__main__":
    main()
