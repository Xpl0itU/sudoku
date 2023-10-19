from typing import List

from src.check_square import check_square
from src.check_rows import check_rows
from src.check_columns import check_columns, get_column_count
from src.check_nums import check_nums


def check_sudoku(sudoku: List[List[int]]) -> bool:
    columns = get_column_count(sudoku)
    return (
        check_square(sudoku, columns)
        and check_rows(sudoku)
        and check_columns(sudoku)
        and check_nums(sudoku, columns)
    )


if __name__ == "__main__":
    import tests.sudoku_tests

    tests = [
        tests.sudoku_tests.get_correct_test(),
        tests.sudoku_tests.get_out_of_range_lower_not_square_incorrect_test(),
        tests.sudoku_tests.get_out_of_range_upper_incorrect_test(),
        tests.sudoku_tests.get_repeating_col_incorrect_test(),
        tests.sudoku_tests.get_repeating_row_col_incorrect_test(),
        tests.sudoku_tests.get_string_incorrect_test(),
    ]
    for test, expected_value in tests:
        print(f"{check_sudoku(test)}, expected value: {expected_value}")
