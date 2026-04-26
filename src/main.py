from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from .summary_engine import build_summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a quick summary for a CSV file.")
    parser.add_argument("csv_path", type=Path, help="Input CSV file.")
    parser.add_argument("--json-out", type=Path, help="Optional path to save summary as JSON.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    frame = pd.read_csv(args.csv_path)
    summary = build_summary(frame)

    print(f"Rows: {summary['shape']['rows']}")
    print(f"Columns: {summary['shape']['columns']}")
    print(f"Numeric columns: {len(summary['column_groups']['numeric'])}")
    print(f"Categorical columns: {len(summary['column_groups']['categorical'])}")
    print(f"Datetime-like columns: {len(summary['column_groups']['datetime_like'])}")

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"Summary JSON written to: {args.json_out}")


if __name__ == "__main__":
    main()
