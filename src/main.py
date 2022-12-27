import pygame
from functools import reduce
from src.constants import blocksize, BLACK, WHITE, GREEN, RED, matrix2, gridDisplay
from src.game_of_life.game_of_life import GameOfLife
from src.game_of_life.game_of_life_constants import G_Constant
from src.utils.drawing import square

pygame.init()
pygame.display.set_caption("A* Algorithm")

# globals
not_traversable = []

matrix2 = list(map(list, zip(*matrix2)))  # rotate


def writeBlackAndWhiteSquares():
    y = 0
    for row in matrix2:
        x = 0
        for item in row:
            if item == 0:
                square(x, y, color=WHITE, blocksize=blocksize, surface=gridDisplay)
            else:
                square(x, y, color=WHITE, blocksize=blocksize, surface=gridDisplay)

            x += blocksize
        y += blocksize
    pygame.display.update()


def set_cell_untraversable(mouse_click_event):
    # determine mouse position
    _mpos_x, _mpos_y = mouse_click_event.pos
    # determine cell number
    coordinate = _mpos_x // blocksize, _mpos_y // blocksize
    rect = pygame.Rect(
        coordinate[0] * blocksize, coordinate[1] * blocksize, blocksize, blocksize
    )
    pygame.draw.rect(gridDisplay, BLACK, rect)
    not_traversable.append(coordinate)
    matrix2[coordinate[0]][coordinate[1]] = -1


def compute_rect_from_mouse_position(mouse_Clicked_Event):
    # determine mouse position
    _mpos_x, _mpos_y = mouse_Clicked_Event.pos
    # determine cell number
    coordinate = _mpos_x // blocksize, _mpos_y // blocksize
    rect = pygame.Rect(
        coordinate[0] * blocksize, coordinate[1] * blocksize, blocksize, blocksize
    )
    return rect, coordinate


def set_start_point(start_point_Event):
    rect, coordinate = compute_rect_from_mouse_position(start_point_Event)
    pygame.draw.rect(gridDisplay, RED, rect)
    not_traversable.append(coordinate)
    t1, t2 = coordinate
    matrix2[t1][t2] = -1


def set_end_point(end_point_Event):
    rect, coordinate = compute_rect_from_mouse_position(end_point_Event)
    pygame.draw.rect(gridDisplay, GREEN, rect)
    not_traversable.append(coordinate)
    matrix2[coordinate[0]][coordinate[1]] = -1


# As a quick-n-dirty solution to get somewhat unstable C-style index[i][j] access
def get_recursive(lst, idx_list):
    """Use like this:
    y = [[3, 1], [2, 7]]
    get_recursive(y, [0, 0]) == 3
    """
    return reduce(list.__getitem__, [lst, *idx_list])


# gonna write a function to predict the h-cost and G-cost
# G-cost = distance from starting node.
# H-cost = distance from end node.

# def calculate_Cost():


def main():
    global event
    writeBlackAndWhiteSquares()
    running = True
    search_started = False
    start_and_entpoint_set = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (
                    event.button == 1 and not search_started
                ):  # left click, => and prevent click during execution phase
                    set_cell_untraversable(event)  # creating a block in the grid.
                if event.button == 3:  # right click
                    start_and_entpoint_set += 1
                    if start_and_entpoint_set == 1:
                        set_start_point(event)
                        print("Setting start Point.")
                    if start_and_entpoint_set == 2:
                        print("Setting end Point.")
                        set_end_point(event)
            pygame.display.update()
        if start_and_entpoint_set == 2:
            # This means we can start the actual alorithm.
            search_started = True
            print("starting search ")
            # run the algorithm here


def game_of_life():
    constants = G_Constant()
    game = GameOfLife(constants)  # noinspection PyArgumentList


if __name__ == "__main__":
    game_of_life()
