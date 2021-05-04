import pygame
from helpers import colors, physics
from classes.player import Player
from classes.stars import Stars
from classes.pipe import Pipe
import numpy as np


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

run = True

stars = Stars(surface=win, star_count=1000, star_movement=[-2, 0.1])


def init_game():
    pipe_gap = 350
    pipe_width = 100

    n_pipes = 2

    player = Player(win)
    pipes = [
        Pipe(surface=win, pipe_gap=pipe_gap, pipe_width=pipe_width)
        for i in range(n_pipes)
    ]

    for i in range(n_pipes):
        pipes[i].rect1.x += i * (screen_width + 100) / (n_pipes)
        pipes[i].rect2.x += i * (screen_width + 100) / (n_pipes)

    points = 0

    return player, pipes, points, pipe_gap, pipe_width


def main_loop(points, pipe_gap, pipe_width, clock_ticks):
    collided = False
    win.fill(colors.BACKGROUND)
    pygame.time.delay(40)
    stars.update_and_draw(win)
    for pipe in pipes:
        pipe.update_and_draw(win)
        if physics.check_collision(player, pipe):
            collided = True

        if pipe.rect1.x < 0 - pipe.width:
            if pipe_gap > 160:
                pipe_gap -= 5
            if pipe_width > 10:
                pipe_width -= 1.5

            pipe.reset(win, pipe_gap, pipe_width)

    stars.star_movement = [-1, -0.005 * player.vel_y]

    points += (pygame.time.get_ticks() - clock_ticks) / 100000

    player.draw(win)

    text = font.render(f"points: {int(points)}", 5, (255, 255, 255))
    win.blit(text, (10, 10))

    player.update()
    pygame.display.update()
    return points, pipe_gap, pipe_width, collided


def final_screen(points, highscore):
    stars.star_movement = [-0.2, -0]
    win.fill(colors.BACKGROUND)
    stars.update_and_draw(win)
    texts = []
    texts.append(font_big.render(f"Final points: {int(points)}", 5, (255, 255, 255)))
    texts.append(font_big.render(f"Highscore: {int(highscore)}", 5, (255, 255, 255)))
    texts.append(font.render("Press R to restart", 5, (255, 255, 255)))

    text_rect = texts[0].get_rect(center=(screen_width / 2, screen_height / 2))

    for i in range(len(texts)):
        win.blit(texts[i], text_rect.move((0, 100 * (i - len(texts) / 2))))
    pygame.display.update()


is_main_loop = True

player, pipes, points, pipe_gap, pipe_width = init_game()

highscore = 0

clock_ticks = 0

while run:
    if is_main_loop:
        points, pipe_gap, pipe_width, collided = main_loop(
            points, pipe_gap, pipe_width, clock_ticks
        )
        if collided:
            is_main_loop = False
    else:
        if points > highscore:
            highscore = points
        final_screen(points, highscore)
        key = pygame.key.get_pressed()

        if key[pygame.K_r]:
            clock_ticks = pygame.time.get_ticks()
            player, pipes, points, pipe_gap, pipe_width = init_game()
            is_main_loop = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
