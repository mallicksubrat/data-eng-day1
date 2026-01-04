import pytest
import tempfile
import csv
from pathlib import Path

from src.csv_to_json.reader import read_csv, CSVReadError


def test_read_csv_success():
    """Test successful CSV reading."""
    # Create temporary CSV
    data = [["name", "age"], ["Alice", "25"], ["Bob", "30"]]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        writer = csv.writer(f)
        writer.writerows(data)
        temp_path = f.name

    try:
        result = read_csv(temp_path)
        assert len(result) == 2
        assert result[0]["name"] == "Alice"
        assert result[0]["age"] == "25"
        assert result[1]["name"] == "Bob"
        assert result[1]["age"] == "30"
    finally:
        Path(temp_path).unlink()


def test_read_csv_file_not_found():
    """Test error when file doesn't exist."""
    with pytest.raises(CSVReadError, match="File not found"):
        read_csv("nonexistent.csv")


def test_read_csv_empty_file():
    """Test error when CSV file has only headers."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("name,age\n")  # Only header
        temp_path = f.name

    try:
        with pytest.raises(CSVReadError, match="CSV file is empty"):
            read_csv(temp_path)
    finally:
        Path(temp_path).unlink()


def test_read_csv_with_sample_data():
    """Test reading with actual sample data structure."""
    # Create CSV with structure similar to sample_data/input.csv
    data = [
        ["Year", "Industry_name_NZSIOC", "Value"],
        ["2024", "All industries", "979594"],
        ["2023", "Manufacturing", "123456"],
    ]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        writer = csv.writer(f)
        writer.writerows(data)
        temp_path = f.name

    try:
        result = read_csv(temp_path)
        assert len(result) == 2
        assert result[0]["Year"] == "2024"
        assert result[0]["Industry_name_NZSIOC"] == "All industries"
        assert result[0]["Value"] == "979594"
    finally:
        Path(temp_path).unlink()
