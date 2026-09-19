"""Create leakage-safe normalized virality labels."""
from __future__ import annotations

import argparse
import numpy as np
import pandas as pd


def build_labels(df: pd.DataFrame, viral_quantile: float = 0.80) -> pd.DataFrame:
    out = df.copy()
    if "views_7d" not in out.columns:
        raise ValueError("Expected a fixed-horizon target column: views_7d")

    if "creator_median_views_prev10" in out.columns:
        baseline = out["creator_median_views_prev10"].fillna(out["views_7d"].median())
        out["breakout_score"] = np.log1p(out["views_7d"]) - np.log1p(baseline.clip(lower=0))
    else:
        out["breakout_score"] = np.log1p(out["views_7d"])

    threshold = out["breakout_score"].quantile(viral_quantile)
    out["viral_label"] = (out["breakout_score"] >= threshold).astype(int)
    out.attrs["viral_threshold"] = float(threshold)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--viral-quantile", type=float, default=0.80)
    args = p.parse_args()

    df = pd.read_csv(args.input)
    out = build_labels(df, args.viral_quantile)
    out.to_csv(args.output, index=False)
    print(f"Wrote {len(out):,} labeled rows -> {args.output}")


if __name__ == "__main__":
    main()
