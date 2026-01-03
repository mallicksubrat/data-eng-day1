# data-eng-day1

## What this does

This project implements a small production-style data pipeline that reads a CSV file, validates its schema, and writes deterministic JSONL output.  
The focus is on clean code structure, explicit error handling, idempotent writes, and unit testing — not on data size or tooling.

The pipeline is intentionally simple to demonstrate core data engineering fundamentals that matter in real systems.

---

## Pipeline flow

1. Read input CSV file
2. Validate required schema
3. Write output as JSON Lines (one JSON object per line)

---

## How to run

From the repository root:

```bash
python -m src.csv_to_jsonl.main \
  --input sample_data/input.csv \
  --output output.jsonl
