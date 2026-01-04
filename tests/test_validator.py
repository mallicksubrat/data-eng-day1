import pytest
from src.csv_to_json.validator import validate_row, validate_data, ValidationError


def test_validate_row_success():
    """Test successful row validation."""
    row = {"Year": "2024", "Industry_name_NZSIOC": "All industries", "Value": "979594"}
    # Should not raise any exception
    validate_row(row)


def test_validate_row_missing_required_field():
    """Test validation fails with missing required field."""
    row = {
        "Year": "2024",
        "Value": "979594",
        # Missing Industry_name_NZSIOC
    }
    with pytest.raises(
        ValidationError, match="Missing required field: Industry_name_NZSIOC"
    ):
        validate_row(row)


def test_validate_row_empty_required_field():
    """Test validation fails with empty required field."""
    row = {
        "Year": "2024",
        "Industry_name_NZSIOC": "",  # Empty
        "Value": "979594",
    }
    with pytest.raises(
        ValidationError, match="Missing required field: Industry_name_NZSIOC"
    ):
        validate_row(row)


def test_validate_row_invalid_year():
    """Test validation fails with non-numeric year."""
    row = {
        "Year": "invalid",
        "Industry_name_NZSIOC": "All industries",
        "Value": "979594",
    }
    with pytest.raises(ValidationError, match="Year must be numeric"):
        validate_row(row)


def test_validate_row_invalid_value():
    """Test validation fails with non-numeric value."""
    row = {"Year": "2024", "Industry_name_NZSIOC": "All industries", "Value": "invalid"}
    with pytest.raises(ValidationError, match="Value must be numeric"):
        validate_row(row)


def test_validate_data_success():
    """Test successful data validation."""
    data = [
        {"Year": "2024", "Industry_name_NZSIOC": "All industries", "Value": "979594"},
        {"Year": "2023", "Industry_name_NZSIOC": "Manufacturing", "Value": "123456"},
    ]
    result = validate_data(data)
    assert len(result) == 2


def test_validate_data_with_invalid_rows():
    """Test data validation with some invalid rows."""
    data = [
        {"Year": "2024", "Industry_name_NZSIOC": "All industries", "Value": "979594"},
        {
            "Year": "invalid",  # Invalid year
            "Industry_name_NZSIOC": "Manufacturing",
            "Value": "123456",
        },
        {"Year": "2022", "Industry_name_NZSIOC": "Retail", "Value": "789012"},
    ]
    result = validate_data(data)
    # Should return only valid rows (first and third)
    assert len(result) == 2
    assert result[0]["Year"] == "2024"
    assert result[1]["Year"] == "2022"
