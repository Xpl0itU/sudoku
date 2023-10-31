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
