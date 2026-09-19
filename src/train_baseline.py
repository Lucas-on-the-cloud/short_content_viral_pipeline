"""Creator-grouped regression baseline for processed tabular/embedding features."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from scipy.stats import spearmanr


def numeric_feature_columns(df: pd.DataFrame, target: str, group: str) -> list[str]:
    blocked = {
        target,
        group,
        "viral_label",
        "views_7d",
        "likes_7d",
        "comments_7d",
        "shares_7d",
    }
    return [c for c in df.select_dtypes(include=[np.number]).columns if c not in blocked]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--target", default="breakout_score")
    p.add_argument("--group", default="creator_id")
    p.add_argument("--output", default="outputs/baseline_metrics.json")
    args = p.parse_args()

    df = pd.read_csv(args.input)
    if args.target not in df.columns or args.group not in df.columns:
        raise ValueError(f"Need columns {args.target!r} and {args.group!r}")

    features = numeric_feature_columns(df, args.target, args.group)
    if not features:
        raise ValueError("No numeric model features found after leakage-safe filtering.")

    splitter = GroupShuffleSplit(n_splits=1, test_size=0.20, random_state=42)
    train_idx, test_idx = next(splitter.split(df, groups=df[args.group]))
    train, test = df.iloc[train_idx], df.iloc[test_idx]

    model = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
        ("regressor", HistGradientBoostingRegressor(random_state=42)),
    ])
    model.fit(train[features], train[args.target])
    pred = model.predict(test[features])

    metrics = {
        "n_train": int(len(train)),
        "n_test": int(len(test)),
        "n_features": int(len(features)),
        "mae": float(mean_absolute_error(test[args.target], pred)),
        "rmse": float(mean_squared_error(test[args.target], pred) ** 0.5),
        "r2": float(r2_score(test[args.target], pred)),
        "spearman": float(spearmanr(test[args.target], pred).statistic),
        "features": features,
    }

    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
