import pygame
pygame.init()
pygame.display.set_caption('A* Algorithm')
blocksize = 50
gridDisplay = pygame.display.set_mode((200, 200))
pygame.display.get_surface().fill((200, 100, 200))  # background
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

matrix = [[1, 1, 0, 1],
          [1, 0, 0, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 1]]


not_traversable = []



# To declare a multidimensional list of zeros in python you have to use a list comprehension like this:
matrix2 = [[0 for col in range(4)] for row in range(4)]
# to avoid reference sharing between the rows.


def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, blocksize, blocksize])


def visualizeGrid():
    y = 0
    for row in matrix2:
        x = 0
        for item in row:
            if item == 0:
                createSquare(x, y, (255, 255, 255))
            else:
                createSquare(x, y, (0, 0, 0))
            x += blocksize
        y += blocksize
    pygame.display.update()

def set_Cell_untravsersable(mouse_click_event):
    # determine mouse position
    _mpos_x, _mpos_y = mouse_click_event.pos
    # determine cell number
    coordinate = _mpos_x // blocksize, _mpos_y // blocksize
    rect = pygame.Rect(coordinate[0] * blocksize, coordinate[1] * blocksize,
                       blocksize, blocksize)
    pygame.draw.rect(gridDisplay, BLACK, rect)
    not_traversable.append(coordinate)


visualizeGrid()  # call the function

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            set_Cell_untravsersable(event)
        pygame.display.update()
