import test.common_tests as common_tests

import pytest
from src.check_nums import check_nums
from src.check_columns import get_column_count


@pytest.mark.nums
def test_nums_validates_correct_nums():
    assert (
        check_nums(
            common_tests.get_correct_test()[0],
            get_column_count(common_tests.get_correct_test()[0]),
        )
        == common_tests.get_correct_test()[1]
    )


@pytest.mark.nums
def test_nums_rejects_float_nums():
    assert (
        check_nums(
            common_tests.get_float_incorrect_test()[0],
            get_column_count(common_tests.get_float_incorrect_test()[0]),
        )
        == common_tests.get_float_incorrect_test()[1]
    )


@pytest.mark.nums
def test_nums_rejects_out_of_range_lower_not_square_nums():
    assert (
        check_nums(
            common_tests.get_out_of_range_lower_not_square_incorrect_test()[0],
            get_column_count(
                common_tests.get_out_of_range_lower_not_square_incorrect_test()[0]
            ),
        )
        == common_tests.get_out_of_range_lower_not_square_incorrect_test()[1]
    )


@pytest.mark.nums
def test_nums_rejects_out_of_range_upper_nums():
    assert (
        check_nums(
            common_tests.get_out_of_range_upper_incorrect_test()[0],
            get_column_count(common_tests.get_out_of_range_upper_incorrect_test()[0]),
        )
        == common_tests.get_out_of_range_upper_incorrect_test()[1]
    )


@pytest.mark.nums
def test_nums_rejects_strings():
    assert (
        check_nums(
            common_tests.get_out_of_range_upper_incorrect_test()[0],
            get_column_count(common_tests.get_out_of_range_upper_incorrect_test()[0]),
        )
        == common_tests.get_out_of_range_upper_incorrect_test()[1]
    )
