import test.common_tests as common_tests

import pytest
from src.check_columns import check_columns


@pytest.mark.columns
def test_columns_validates_correct_col():
    assert (
        check_columns(common_tests.get_correct_test()[0])
        == common_tests.get_correct_test()[1]
    )


@pytest.mark.columns
def test_columns_rejects_repeating_col():
    assert (
        check_columns(common_tests.get_repeating_col_incorrect_test()[0])
        == common_tests.get_repeating_col_incorrect_test()[1]
    )


@pytest.mark.columns
def test_columns_rejects_repeating_row_col():
    assert (
        check_columns(common_tests.get_repeating_row_col_incorrect_test()[0])
        == common_tests.get_repeating_row_col_incorrect_test()[1]
    )
