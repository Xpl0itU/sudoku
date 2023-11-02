import test.common_tests as common_tests

import pytest
from src.check_square import check_square
from src.check_columns import get_column_count


@pytest.mark.square
def test_square_validates_correct_square():
    assert (
        check_square(
            common_tests.get_correct_test().sudoku_to_test,
            get_column_count(common_tests.get_correct_test().sudoku_to_test),
        )
        == common_tests.get_correct_test().expected_result
    )


@pytest.mark.square
def test_square_rejects_not_square():
    assert (
        check_square(
            common_tests.get_out_of_range_lower_not_square_incorrect_test().sudoku_to_test,
            get_column_count(
                common_tests.get_out_of_range_lower_not_square_incorrect_test().sudoku_to_test
            ),
        )
        == common_tests.get_out_of_range_lower_not_square_incorrect_test().expected_result
    )
