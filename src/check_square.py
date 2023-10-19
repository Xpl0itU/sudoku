from typing import List


def check_square(sudoku: List[List[int]], columns: int) -> bool:
    rows = len(sudoku[0])
    if columns != rows:
        return False
    for row in sudoku:
        if len(row) != rows:
            return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import tests.sudoku_tests
    import src.check_columns

    tests = [
        tests.sudoku_tests.get_correct_test(),
        tests.sudoku_tests.get_out_of_range_lower_not_square_incorrect_test(),
    ]
    for test, expected_value in tests:
        print(
            f"{check_square(test, src.check_columns.get_column_count(test))}, expected value: {expected_value}"
        )
