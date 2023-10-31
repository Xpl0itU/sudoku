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
