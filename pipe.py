import pygame
from helpers import colors
import numpy as np


class Pipe(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.bounds = surface.get_size()
        self.width, self.height = 100, 350
        self.rect1 = pygame.rect.Rect((self.bounds[0], 0, self.width, self.height))
        self.rect2 = pygame.rect.Rect((self.bounds[0], 500, self.width, self.height))
        self.vel_x = 10

    def update_and_draw(self, surface):
        self.rect1.x -= self.vel_x
        self.rect2.x -= self.vel_x

        if self.rect1.x + self.width < 0:
            self.rect1.x = self.bounds[0] + self.width
            self.rect2.x = self.bounds[0] + self.width
            rnd = (np.random.random() - 1) * 25
            self.rect1.y += rnd
            self.rect2.y += rnd

        pygame.draw.rect(surface, colors.LIGHT, self.rect1)
        pygame.draw.rect(surface, colors.LIGHT, self.rect2)

    def __del__(self):
        print("pipe deleted")
