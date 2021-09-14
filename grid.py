import pygame

pygame.init()
pygame.display.set_caption('A* Algorithm')
blocksize = 50
NUMBER_OF_BOXES = 25  # boxes per line
LENGTH = NUMBER_OF_BOXES * blocksize
gridDisplay = pygame.display.set_mode((LENGTH, LENGTH))
pygame.display.get_surface().fill((200, 100, 200))  # background

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

not_traversable = []

matrix2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(matrix2)
matrix2 = list(map(list, zip(*matrix2)))
print(matrix2)


def initializeGrid():
    linesize = 20  # Later, introduce this, so you can see the walls between the grids.

    y = 0
    for row in matrix2:
        x = 0
        for item in row:
            if item == 0:
                createSquare(x, y, WHITE)
            else:
                createSquare(x, y, BLACK)
            x += blocksize
        y += blocksize
    pygame.display.update()


def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, blocksize, blocksize])


def createLine(x1, y1, x2, y2):
    pygame.draw.line(gridDisplay, BLACK, (x1, y1), (x2, y2))
    pygame.display.flip()


def compute_Rectangle_From_MousePosition(mouse_Clicked_Event):
    # determine mouse position
    _mpos_x, _mpos_y = mouse_Clicked_Event.pos
    # determine cell number
    coordinate = _mpos_x // blocksize, _mpos_y // blocksize
    rect = pygame.Rect(coordinate[0] * blocksize, coordinate[1] * blocksize,
                       blocksize, blocksize)
    return rect, coordinate


def set_Cell_untraversable(mouse_click_event):
    # determine mouse position
    _mpos_x, _mpos_y = mouse_click_event.pos
    # determine cell number
    coordinate = _mpos_x // blocksize, _mpos_y // blocksize
    rect = pygame.Rect(coordinate[0] * blocksize, coordinate[1] * blocksize,
                       blocksize, blocksize)
    pygame.draw.rect(gridDisplay, BLACK, rect)
    not_traversable.append(coordinate)
    matrix2[coordinate[0]][coordinate[1]] = -1


def set_start_Point(start_point_Event):
    rect, coordinate = compute_Rectangle_From_MousePosition(start_point_Event)
    pygame.draw.rect(gridDisplay, RED, rect)
    not_traversable.append(coordinate)
    matrix2[coordinate[0]][coordinate[1]] = -1


def set_end_Point(end_point_Event):
    rect, coordinate = compute_Rectangle_From_MousePosition(end_point_Event)
    pygame.draw.rect(gridDisplay, GREEN, rect)
    not_traversable.append(coordinate)
    matrix2[coordinate[0]][coordinate[1]] = -1


if __name__ == "__main__":
    initializeGrid()

    running = True
    Algo_is_running = False
    # I think I have to introduce another boolean value.
    # It's probably necessary, because I have to call the A* algorithm function in the Loop only once.

    count_right_clicks = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not Algo_is_running:  # left click, and prevent click during execution phase
                    set_Cell_untraversable(event)  # creating a block in the grid.
                if event.button == 3:  # right click
                    count_right_clicks += 1
                    if count_right_clicks == 1:
                        set_start_Point(event)
                        print("Setting start Point.")
                    if count_right_clicks == 2:
                        print("Setting end Point.")
                        set_end_Point(event)
            pygame.display.update()
        if count_right_clicks == 2:
            # Start- and endpoint set. Start the Algorithm. . .
            Algo_is_running = True

            print("starting - ")
