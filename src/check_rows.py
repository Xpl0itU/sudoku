from typing import List


def check_rows(sudoku: List[List[int]]) -> bool:
    for row in sudoku:
        for num in row:
            if row.count(num) > 1:
                return False
    return True


if __name__ == "__main__":
    import sys

    sys.path.append("..")

    import tests.sudoku_tests

    tests = [
        tests.sudoku_tests.get_correct_test(),
        tests.sudoku_tests.get_repeating_row_col_incorrect_test(),
    ]
    for test, expected_value in tests:
        print(f"{check_rows(test)}, expected value: {expected_value}")
