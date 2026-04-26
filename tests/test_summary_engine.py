import pandas as pd

from src.summary_engine import build_summary


def test_build_summary() -> None:
    frame = pd.DataFrame(
        {
            "value": [1, 2, 3, 4],
            "category": ["a", "b", "a", None],
            "created_at": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"],
        }
    )
    summary = build_summary(frame)

    assert summary["shape"]["rows"] == 4
    assert "value" in summary["column_groups"]["numeric"]
    assert "created_at" in summary["column_groups"]["datetime_like"]
    assert summary["missing_values"]["category"] == 1
