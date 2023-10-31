from typing import List


def check_rows(sudoku: List[List[int]]) -> bool:
    for row in sudoku:
        for num in row:
            if row.count(num) > 1:
                return False
    return True
