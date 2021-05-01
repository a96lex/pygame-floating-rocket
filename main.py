import pygame
from helpers import colors
from player import Player
from stars import Stars
import numpy as np


pygame.init()

screen_width, screen_height = 1080, 720

win = pygame.display.set_mode((screen_width, screen_height))

run = True

player = Player(win)
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
    player.draw(win)
    player.update()
    pygame.display.update()

pygame.quit()