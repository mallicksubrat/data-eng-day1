import json
import tempfile
from pathlib import Path

from src.csv_to_json.writer import write_json, write_json_lines


def test_write_json():
    """Test writing data to JSON file."""
    data = [{"name": "Alice", "age": "25"}, {"name": "Bob", "age": "30"}]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        temp_path = f.name

    try:
        write_json(data, temp_path)

        # Read back and verify
        with open(temp_path, "r", encoding="utf-8") as f:
            result = json.load(f)

        assert result == data
    finally:
        Path(temp_path).unlink()


def test_write_json_creates_directory():
    """Test that write_json creates parent directories if they don't exist."""
    data = [{"test": "data"}]

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "subdir" / "output.json"

        write_json(data, str(output_path))

        assert output_path.exists()
        with open(output_path, "r", encoding="utf-8") as f:
            result = json.load(f)
        assert result == data


def test_write_json_lines():
    """Test writing data to JSON Lines format."""
    data = [{"name": "Alice", "age": "25"}, {"name": "Bob", "age": "30"}]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        temp_path = f.name

    try:
        write_json_lines(data, temp_path)

        # Read back and verify
        result = []
        with open(temp_path, "r", encoding="utf-8") as f:
            for line in f:
                result.append(json.loads(line.strip()))

        assert result == data
    finally:
        Path(temp_path).unlink()


def test_write_json_lines_creates_directory():
    """Test that write_json_lines creates parent directories if they don't exist."""
    data = [{"test": "data"}]

    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "subdir" / "output.jsonl"

        write_json_lines(data, str(output_path))

        assert output_path.exists()
        result = []
        with open(output_path, "r", encoding="utf-8") as f:
            for line in f:
                result.append(json.loads(line.strip()))
        assert result == data


def test_write_json_with_unicode():
    """Test writing JSON with Unicode characters."""
    data = [
        {"name": "José", "city": "São Paulo"},
        {"name": "Björk", "city": "Reykjavík"},
    ]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        temp_path = f.name

    try:
        write_json(data, temp_path)

        # Read back and verify
        with open(temp_path, "r", encoding="utf-8") as f:
            result = json.load(f)

        assert result == data
    finally:
        Path(temp_path).unlink()
