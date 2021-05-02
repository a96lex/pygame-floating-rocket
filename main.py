import pygame
from helpers import colors, physics
from player import Player
from stars import Stars
from pipe import Pipe
import numpy as np


pygame.init()

screen_width, screen_height = 1080, 720

win = pygame.display.set_mode((screen_width, screen_height))

run = True

pipe_gap = 350
pipe_width = 100
pipe_speed = 10

n_pipes = 2

player = Player(win)
pipes = [
    Pipe(surface=win, pipe_gap=pipe_gap, pipe_width=pipe_width) for i in range(n_pipes)
]

for i in range(n_pipes):
    pipes[i].rect1.x += i * (screen_width + 100) / (n_pipes)
    pipes[i].rect2.x += i * (screen_width + 100) / (n_pipes)

stars = Stars(surface=win, star_count=1000, star_movement=[-2, 0.1])


while run:
    win.fill(colors.BG)
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    stars.update_and_draw(win)
    collided = False
    for pipe in pipes:
        pipe.update_and_draw(win)
        if physics.check_collision(player, pipe):
            player.color = colors.FIRE
            collided = True
        if pipe.rect1.x < 0 - pipe.width:
            if pipe_gap > 160:
                pipe_gap -= 5
            if pipe_width > 10:
                pipe_width -= 1.5

            pipe.reset(win, pipe_gap, pipe_width)

    stars.star_movement = [-1, -0.005 * player.vel_y]

    if not collided:
        player.color = colors.LIGHT

    player.draw(win)
    player.update()
    pygame.display.update()

pygame.quit()