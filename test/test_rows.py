import test.common_tests as common_tests

import pytest
from src.check_rows import check_rows


@pytest.mark.rows
def test_rows_validates_correct_rows():
    assert (
        check_rows(
            common_tests.get_correct_test().sudoku_to_test,
        )
        == common_tests.get_correct_test().expected_result
    )


@pytest.mark.rows
def test_rows_rejects_repeating_row_col():
    assert (
        check_rows(common_tests.get_repeating_row_col_incorrect_test().sudoku_to_test)
        == common_tests.get_repeating_row_col_incorrect_test().expected_result
    )
