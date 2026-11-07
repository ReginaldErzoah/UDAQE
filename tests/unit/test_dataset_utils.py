import pytest
from udaqe.dataset_utils import get_file_format


@pytest.mark.parametrize(
        "file_path, expected",
        [
            ("customer.csv","csv"),
            ("sales.XLSX","xlsx"),
            ("customers.JSON","json"),
            ("customers.backup.csv","csv"),
        ],
)
def test_get_file_format(file_path,expected):
    assert get_file_format(file_path) == expected


def test_missing_extension():
    with pytest.raises(ValueError):
        get_file_format("customers")


def test_trailing_dot():
    with pytest.raises(ValueError):
        get_file_format("customers.")
