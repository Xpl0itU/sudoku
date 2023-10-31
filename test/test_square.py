import test.common_tests as common_tests

import pytest
from src.check_square import check_square
from src.check_columns import get_column_count


@pytest.mark.square
def test_square_validates_correct_square():
    assert (
        check_square(
            common_tests.get_correct_test()[0],
            get_column_count(common_tests.get_correct_test()[0]),
        )
        == common_tests.get_correct_test()[1]
    )


@pytest.mark.square
def test_square_rejects_not_square():
    assert (
        check_square(
            common_tests.get_out_of_range_lower_not_square_incorrect_test()[0],
            get_column_count(
                common_tests.get_out_of_range_lower_not_square_incorrect_test()[0]
            ),
        )
        == common_tests.get_out_of_range_lower_not_square_incorrect_test()[1]
    )
