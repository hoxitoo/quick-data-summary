# Quick Data Summary

A compact command-line tool that turns any CSV file into a readable summary report.

## What it does

- detects row and column counts
- shows data types
- counts missing values
- generates numeric statistics
- highlights top values in categorical columns
- exports a JSON report

## Why this project matters

A lot of real work starts with one messy CSV file.  
This tool helps analysts and developers get fast situational awareness before deeper analysis.

## Usage

```bash
python -m src.main examples/sales.csv --json-out outputs/summary.json
```

## Example output

```text
Rows: 6
Columns: 5
Numeric columns: 2
Categorical columns: 2
Datetime-like columns: 1
```

## Testing

```bash
pytest
```
