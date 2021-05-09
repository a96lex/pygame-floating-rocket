import pygame
import numpy as np
import sys
from classes.game import Game


game = Game()

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
