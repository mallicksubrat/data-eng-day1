from typing import List, Dict, Any


class ValidationError(Exception):
    pass


def validate_row(row: Dict[str, Any]) -> None:
    """Validate a single CSV row."""
    required_fields = ["Year", "Industry_name_NZSIOC", "Value"]

    for field in required_fields:
        if field not in row or not row[field]:
            raise ValidationError(f"Missing required field: {field}")

    # Validate Year is numeric
    if not str(row.get("Year", "")).isdigit():
        raise ValidationError("Year must be numeric")

    # Validate Value is numeric
    try:
        float(row.get("Value", ""))
    except (ValueError, TypeError):
        raise ValidationError("Value must be numeric")


def validate_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate entire dataset and return cleaned data."""
    validated_data = []

    for i, row in enumerate(data):
        try:
            validate_row(row)
            validated_data.append(row)
        except ValidationError as e:
            print(f"Warning: Row {i + 1} failed validation: {e}")
            # Skip invalid rows or handle as needed

    return validated_data
