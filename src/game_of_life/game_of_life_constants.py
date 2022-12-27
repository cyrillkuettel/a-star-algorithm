from dataclasses import dataclass
from functools import reduce
""" Bunch of constants for this pygame instance """


@dataclass
class G_Constant:

    # initial Grid
    matrix = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    white = (255, 255, 255)
    black = (0, 0, 0)

    num_rows = len(matrix)
    num_cols = len([item[0] for item in matrix])

    # num_cols = get_recursive(matrix, [0, 0])

    num_boxes: int =len(reduce(lambda a, b: a + b, matrix))

    scale: int = 50  # scales the whole window
    width: int = num_boxes * 20
    height: int = num_boxes * 20

    background: tuple[int, int, int] = black

