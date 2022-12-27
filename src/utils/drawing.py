import pygame


def square(x, y, color, blocksize, surface):
    pygame.draw.rect(surface, color, [x, y, blocksize, blocksize])


def line(x1, y1, x2, y2, surface, color=(0, 0, 0)):
    pygame.draw.line(surface, color, (x1, y1), (x2, y2))
    pygame.display.flip()
