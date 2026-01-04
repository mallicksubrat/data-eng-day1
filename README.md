# CSV to JSON Converter

A Python application that converts CSV files to JSON format with optional data validation.

## Features

- Convert CSV files to JSON or JSON Lines format
- Optional data validation (Year must be numeric, Value must be numeric)
- Command-line interface
- Comprehensive test suite

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install pytest
   ```

## Usage

### Basic conversion:
```bash
python -m src.csv_to_json.main input.csv output.json
```

### With validation:
```bash
python -m src.csv_to_json.main input.csv output.json --validate
```

### JSON Lines format:
```bash
python -m src.csv_to_json.main input.csv output.jsonl --format jsonl --validate
```

### Help:
```bash
python -m src.csv_to_json.main --help
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

```
data-eng-day1/
├── src/csv_to_json/
│   ├── __init__.py
│   ├── main.py          # CLI interface
│   ├── reader.py        # CSV reading functionality
│   ├── validator.py     # Data validation
│   └── writer.py        # JSON writing functionality
├── tests/
│   ├── test_reader.py
│   ├── test_validator.py
│   └── test_writer.py
├── sample_data/
│   └── input.csv
├── requirements.txt
└── README.md
```

## Validation Rules

When using `--validate`, the following checks are performed:
- `Year` field must be numeric
- `Value` field must be numeric
- Required fields (`Year`, `Industry_name_NZSIOC`, `Value`) must be present and non-empty

Invalid rows are skipped with warning messages.