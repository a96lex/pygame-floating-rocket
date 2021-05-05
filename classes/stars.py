import pygame
import numpy as np
from helpers import colors


class Stars(object):
    def __init__(self, surface, star_count, star_movement, star_size):
        self.bounds = surface.get_size()
        pos_x = np.random.random(size=star_count) * self.bounds[0]
        pos_y = np.random.random(size=star_count) * self.bounds[1]
        self.pos = np.vstack((pos_x, pos_y)).T
        self.size = star_size
        self.star_movement = star_movement

    def update_and_draw(self, surface):
        for star in self.pos:
            pygame.draw.rect(
                surface,
                colors.STARS,
                (int(star[0]), int(star[1]), self.size, self.size),
            )

            star += self.star_movement
            if star[0] > self.bounds[0]:
                star[0] = 0
            if star[0] < 0:
                star[0] = self.bounds[0]
            if star[1] > self.bounds[1]:
                star[1] = 0
            if star[1] < 0:
                star[1] = self.bounds[1]
