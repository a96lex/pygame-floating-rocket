import pygame
from helpers import colors
import numpy as np


class Pipe(pygame.sprite.Sprite):
    def __init__(self, surface, pipe_gap, pipe_width):
        self.bounds = surface.get_size()
        self.width = pipe_width
        self.pipe_gap = pipe_gap
        height1 = np.random.randint(0, high=self.bounds[1] * 0.6)
        height2 = self.bounds[1] - height1 - self.pipe_gap
        self.rect1 = pygame.rect.Rect((self.bounds[0], 0, self.width, height1))
        self.rect2 = pygame.rect.Rect(
            (self.bounds[0], height1 + self.pipe_gap, self.width, height2)
        )
        self.vel_x = 10

    def update_and_draw(self, surface):
        self.rect1.x -= self.vel_x
        self.rect2.x -= self.vel_x

        pygame.draw.rect(surface, colors.PIPE, self.rect1)
        pygame.draw.rect(surface, colors.PIPE, self.rect2)

    def reset(self, surface, pipe_gap, pipe_width):
        self.__init__(surface, pipe_gap, pipe_width)
