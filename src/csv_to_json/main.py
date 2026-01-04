import argparse
import sys
from pathlib import Path

from .reader import read_csv
from .validator import validate_data
from .writer import write_json


def main():
    parser = argparse.ArgumentParser(description="Convert CSV to JSON")
    parser.add_argument("input", help="Input CSV file path")
    parser.add_argument("output", help="Output JSON file path")
    parser.add_argument(
        "--validate", action="store_true", help="Validate data before conversion"
    )
    parser.add_argument(
        "--format",
        choices=["json", "jsonl"],
        default="json",
        help="Output format: json (default) or jsonl (JSON Lines)",
    )

    args = parser.parse_args()

    try:
        # Read CSV
        print(f"Reading CSV from {args.input}...")
        data = read_csv(args.input)
        print(f"Read {len(data)} rows")

        # Validate if requested
        if args.validate:
            print("Validating data...")
            data = validate_data(data)
            print(f"Validated {len(data)} rows")

        # Write JSON
        print(f"Writing {args.format.upper()} to {args.output}...")
        if args.format == "jsonl":
            from .writer import write_json_lines

            write_json_lines(data, args.output)
        else:
            write_json(data, args.output)
        print("Conversion complete!")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
