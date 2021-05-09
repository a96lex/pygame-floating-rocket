import pygame
import numpy as np
import sys


pygame.init()

font = pygame.font.SysFont("ubuntu-mono", 35, True, False)
font_big = pygame.font.SysFont("ubuntu-mono", 70, True, False)

"""
this is for full screen. However objects need to be adjusted to 
current screen size which is not supported at the moment
screen_width, screen_height = (
    pygame.display.Info().current_w,
    pygame.display.Info().current_h,
)
"""

screen_width, screen_height = 1080, 720

win = pygame.display.set_mode((screen_width, screen_height))

game = Game(win=win)

game.init_game()

while True:
    pygame.time.delay(40)

    if game.is_main_loop:
        game.main_loop()
        if game.collided:
            game.is_main_loop = False
    else:
        if game.points > game.highscore:
            game.highscore = game.points
        game.final_screen()

        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            game.init_game()
            game.clock_ticks = pygame.time.get_ticks()
            game.is_main_loop = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


pygame.quit()
