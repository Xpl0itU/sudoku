from typing import List


def check_square(sudoku: List[List[int]], columns: int) -> bool:
    rows = len(sudoku[0])
    if columns != rows:
        return False
    for row in sudoku:
        if len(row) != rows:
            return False
    return True
