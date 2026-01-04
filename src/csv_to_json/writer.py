import json
from pathlib import Path
from typing import List, Dict, Any


def write_json(data: List[Dict[str, Any]], output_path: str) -> None:
    """Write data to JSON file."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_json_lines(data: List[Dict[str, Any]], output_path: str) -> None:
    """Write data as JSON Lines format."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        for row in data:
            json.dump(row, f, ensure_ascii=False)
            f.write("\n")
