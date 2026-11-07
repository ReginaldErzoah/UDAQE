import pytest
from udaqe.dataset_utils import get_file_format

def test_get_file_format():
    assert get_file_format("customer.csv") == "csv"


def test_missing_extension():
    with pytest.raises(ValueError):
        get_file_format("customers")

def test_trailing_dot():
    with pytest.raises(ValueError):
        get_file_format("customers.")


def test_uppercase_extension():
    assert get_file_format("sales.XLSX") == "xlsx"


def test_multiple_dots():
    assert get_file_format("customers.backup.csv") == "csv"


def test_json_extension():
    assert get_file_format("customers.JSON") == "json"