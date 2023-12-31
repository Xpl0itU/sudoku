import test.common_tests as common_tests

import pytest
from src.check_nums import check_nums
from src.check_columns import get_column_count


@pytest.mark.nums
def test_nums_validates_correct_nums():
    assert (
        check_nums(
            common_tests.get_correct_test().sudoku_to_test,
            get_column_count(common_tests.get_correct_test().sudoku_to_test),
        )
        == common_tests.get_correct_test().expected_result
    )


@pytest.mark.nums
def test_nums_rejects_float_nums():
    assert (
        check_nums(
            common_tests.get_float_incorrect_test().sudoku_to_test,
            get_column_count(common_tests.get_float_incorrect_test().sudoku_to_test),
        )
        == common_tests.get_float_incorrect_test().expected_result
    )


@pytest.mark.nums
def test_nums_rejects_out_of_range_lower_not_square_nums():
    assert (
        check_nums(
            common_tests.get_out_of_range_lower_not_square_incorrect_test().sudoku_to_test,
            get_column_count(
                common_tests.get_out_of_range_lower_not_square_incorrect_test().sudoku_to_test
            ),
        )
        == common_tests.get_out_of_range_lower_not_square_incorrect_test().expected_result
    )


@pytest.mark.nums
def test_nums_rejects_out_of_range_upper_nums():
    assert (
        check_nums(
            common_tests.get_out_of_range_upper_incorrect_test().sudoku_to_test,
            get_column_count(
                common_tests.get_out_of_range_upper_incorrect_test().sudoku_to_test
            ),
        )
        == common_tests.get_out_of_range_upper_incorrect_test().expected_result
    )


@pytest.mark.nums
def test_nums_rejects_strings():
    assert (
        check_nums(
            common_tests.get_out_of_range_upper_incorrect_test().sudoku_to_test,
            get_column_count(
                common_tests.get_out_of_range_upper_incorrect_test().sudoku_to_test
            ),
        )
        == common_tests.get_out_of_range_upper_incorrect_test().expected_result
    )
