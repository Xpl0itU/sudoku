from typing import List


def get_column_count(sudoku: List[List[int]]) -> int:
    return len(sudoku)


def check_columns(sudoku: List[List[int]]) -> bool:
    for i, _ in enumerate(sudoku):
        column = [row[i] for row in sudoku]
        for num in column:
            if column.count(num) > 1:
                return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    from tests import sudoku_tests

    tests = [
        sudoku_tests.get_correct_test(),
        sudoku_tests.get_repeating_col_incorrect_test(),
        sudoku_tests.get_repeating_row_col_incorrect_test(),
    ]
    for test, expected_value in tests:
        print(f"{check_columns(test)}, expected value: {expected_value}")
