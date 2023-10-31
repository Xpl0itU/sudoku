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
