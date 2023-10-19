from typing import List


def check_nums(sudoku: List[List[int]], n: int) -> bool:
    for row in sudoku:
        max_row = max(row)
        if not isinstance(max_row, int) or max_row > n:
            return False
        min_row = min(row)
        if not isinstance(min_row, int) or min_row < 1:
            return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import tests.sudoku_tests
    from src.check_columns import get_column_count

    tests = [
        tests.sudoku_tests.get_correct_test(),
        tests.sudoku_tests.get_float_incorrect_test(),
        tests.sudoku_tests.get_out_of_range_lower_not_square_incorrect_test(),
        tests.sudoku_tests.get_out_of_range_upper_incorrect_test(),
        tests.sudoku_tests.get_string_incorrect_test(),
    ]
    for test, expected_value in tests:
        print(
            f"{check_nums(test, get_column_count(test))}, expected value: {expected_value}"
        )