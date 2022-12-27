import pygame

from src.game_of_life.game_of_life_constants import G_Constant
from src.utils.drawing import square


class GameOfLife:
    def __init__(self, constants) -> None:
        super().__init__()
        self._c: G_Constant = constants

        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.surface = pygame.display.set_mode((self._c.width, self._c.height))
        pygame.display.get_surface().fill(self._c.background)

        self.grid_iterator(matrix=self._c.matrix)
        self.game_loop()

    def grid_iterator(self, matrix):
        # for now, disregarding the actual element. Only structure is relevant
        for index_x, _ in enumerate(matrix):
            for index_y, _ in enumerate(matrix):
                _x = self._c.scale * index_x
                _x = 0
                _y = self._c.scale * index_y
                square(
                    x=_x,
                    y=_y,
                    color=self._c.white,
                    blocksize=self._c.scale,
                    surface=self.surface,
                )

    def game_loop(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pygame.display.update()
