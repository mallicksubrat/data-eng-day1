import csv
from pathlib import Path


class CSVReadError(Exception):
    pass


def read_csv(path: str) -> list[dict]:
    file_path = Path(path)

    if not file_path.exists():
        raise CSVReadError(f"File not found: {path}")

    with file_path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise CSVReadError(f"CSV file is empty: {path}")

    return rows
