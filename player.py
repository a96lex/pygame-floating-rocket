import pygame
from helpers import colors


class Player(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.bounds = surface.get_size()
        self.width, self.height = 40, 100
        self.rect = pygame.rect.Rect((10, 10, self.width, self.height))
        self.delta_v = 3
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 9.81
        self.max_speed_y = 40
        self.max_speed_x = 40
        self.going_up = False
        self.color = colors.LIGHT

    def handle_keys(self):
        key = pygame.key.get_pressed()

        self.going_up = False
        if key[pygame.K_LEFT]:
            self.vel_x -= self.delta_v
        if key[pygame.K_RIGHT]:
            self.vel_x += self.delta_v
        if key[pygame.K_UP]:
            self.vel_y -= self.delta_v * 4
            self.going_up = True

    def update(self):
        # handle player input
        self.handle_keys()

        # distance to bottom
        delta_y = self.bounds[1] - self.rect.y - self.height
        if delta_y == 0:
            delta_y += 1

        # add some friction
        self.vel_y *= 0.9

        # apply gravity + repulsion from floor
        self.vel_y += self.gravity - 1000 / delta_y

        # check max velocities
        if self.vel_y < -self.max_speed_y:
            self.vel_y = -self.max_speed_y
        if self.vel_y > self.max_speed_y:
            self.vel_y = self.max_speed_y
        if self.vel_x < -self.max_speed_x:
            self.vel_x = -self.max_speed_x
        if self.vel_x > self.max_speed_x:
            self.vel_x = self.max_speed_x

        # bounce (elastic)
        if (
            self.rect.x + self.vel_x + self.width > self.bounds[0]
            or self.rect.x + self.vel_x < 0
        ):
            self.vel_x = -self.vel_x * 0.4

        if self.rect.y + self.vel_y + 40 < 0:
            self.vel_y = -self.vel_y * 0.4

        # move :)
        self.rect.move_ip((self.vel_x, self.vel_y))

    def invert(self):
        self.vel_x = -self.vel_x * 0.8
        self.vel_y = -self.vel_y * 0.8

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.going_up:
            pygame.draw.rect(
                surface,
                colors.FIRE,
                ((self.rect.x + 5, self.rect.y + self.height, self.width - 10, 10)),
            )
