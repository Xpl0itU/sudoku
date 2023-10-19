from typing import List, Tuple

correct = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

repeating_row_col_incorrect = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]

repeating_col_incorrect = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]

out_of_range_upper_incorrect = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2],
]

string_incorrect = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]

float_incorrect = [[1, 1.5], [1.5, 1]]

out_of_range_lower_not_square_incorrect = [[1, 0, 0, 0], [0, 1, 0], [0, 0, 0, 1]]


def get_correct_test() -> Tuple[List[List[int]], bool]:
    return correct, True


def get_repeating_row_col_incorrect_test() -> Tuple[List[List[int]], bool]:
    return repeating_row_col_incorrect, False


def get_repeating_col_incorrect_test() -> Tuple[List[List[int]], bool]:
    return repeating_col_incorrect, False


def get_out_of_range_upper_incorrect_test() -> Tuple[List[List[int]], bool]:
    return out_of_range_upper_incorrect, False


def get_string_incorrect_test() -> Tuple[List[List[int]], bool]:
    return string_incorrect, False


def get_float_incorrect_test() -> Tuple[List[List[int]], bool]:
    return float_incorrect, False


def get_out_of_range_lower_not_square_incorrect_test() -> Tuple[List[List[int]], bool]:
    return out_of_range_lower_not_square_incorrect, False
