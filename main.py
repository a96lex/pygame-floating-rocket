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

n_pipes = 3

player = Player(win)
pipes = [Pipe(win) for i in range(n_pipes)]

for i in range(n_pipes):
    pipes[i].rect1.x += i * screen_width / (n_pipes)
    pipes[i].rect2.x += i * screen_width / (n_pipes)

stars = Stars(surface=win, star_count=500, star_movement=[1, 0])

# update star velocity at random (for testing)
new_star_vel = [np.random.random() - 0.5, np.random.random() - 0.5]
stars.change_star_movement(star_movement=new_star_vel)

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
    if not collided:
        player.color = colors.LIGHT

    player.draw(win)
    player.update()
    pygame.display.update()

pygame.quit()