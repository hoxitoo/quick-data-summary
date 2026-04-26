from __future__ import annotations

from typing import Any

import pandas as pd


def infer_datetime_columns(frame: pd.DataFrame) -> list[str]:
    detected: list[str] = []
    for col in frame.columns:
        if pd.api.types.is_object_dtype(frame[col]):
            parsed = pd.to_datetime(frame[col], errors="coerce", format="mixed")
            if parsed.notna().mean() >= 0.8:
                detected.append(col)
    return detected


def build_summary(frame: pd.DataFrame) -> dict[str, Any]:
    numeric_columns = frame.select_dtypes(include="number").columns.tolist()
    datetime_columns = infer_datetime_columns(frame)
    categorical_columns = [
        col for col in frame.columns if col not in numeric_columns and col not in datetime_columns
    ]

    numeric_summary = {}
    if numeric_columns:
        numeric_stats = frame[numeric_columns].describe().transpose().fillna(0)
        for col, values in numeric_stats.iterrows():
            numeric_summary[col] = {k: round(float(v), 4) for k, v in values.to_dict().items()}

    categorical_summary = {}
    for col in categorical_columns:
        top_values = frame[col].fillna("<missing>").astype(str).value_counts().head(5)
        categorical_summary[col] = top_values.to_dict()

    missing_values = frame.isna().sum().to_dict()
    dtypes = {col: str(dtype) for col, dtype in frame.dtypes.items()}

    return {
        "shape": {"rows": int(frame.shape[0]), "columns": int(frame.shape[1])},
        "column_groups": {
            "numeric": numeric_columns,
            "categorical": categorical_columns,
            "datetime_like": datetime_columns,
        },
        "dtypes": dtypes,
        "missing_values": {k: int(v) for k, v in missing_values.items()},
        "numeric_summary": numeric_summary,
        "categorical_summary": categorical_summary,
    }
