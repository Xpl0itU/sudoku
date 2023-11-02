import test.common_tests as common_tests

import pytest
from src.check_columns import check_columns


@pytest.mark.columns
def test_columns_validates_correct_col():
    assert (
        check_columns(common_tests.get_correct_test().sudoku_to_test)
        == common_tests.get_correct_test().expected_result
    )


@pytest.mark.columns
def test_columns_rejects_repeating_col():
    assert (
        check_columns(common_tests.get_repeating_col_incorrect_test().sudoku_to_test)
        == common_tests.get_repeating_col_incorrect_test().expected_result
    )


@pytest.mark.columns
def test_columns_rejects_repeating_row_col():
    assert (
        check_columns(
            common_tests.get_repeating_row_col_incorrect_test().sudoku_to_test
        )
        == common_tests.get_repeating_row_col_incorrect_test().expected_result
    )
