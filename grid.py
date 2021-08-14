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


visualizeGrid()  # call the function

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("got into event")
            # determine mouse position
            mpos_x, mpos_y = event.pos
            # determine cell number
            coord = mpos_x // blocksize, mpos_y // blocksize
            print("coord = " + str(coord))

            rect = pygame.Rect(coord[0] * blocksize, coord[1] * blocksize,
                               blocksize, blocksize)
            pygame.draw.rect(gridDisplay, BLACK, rect)
        pygame.display.update()
