import pygame
from helpers import colors
from player import Player
from stars import Stars


pygame.init()

screen_width, screen_height = 1080, 720

win = pygame.display.set_mode((screen_width, screen_height))

run = True

player = Player(win)
close_stars = Stars(surface=win, star_count=100, star_movement=[1, 0], star_size=4)
intermediate_stars = Stars(
    surface=win, star_count=200, star_movement=[0.7, 0], star_size=3
)
far_stars = Stars(surface=win, star_count=300, star_movement=[0.4, 0], star_size=2)

while run:
    win.fill(colors.BG)
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    far_stars.update_and_draw(win)
    intermediate_stars.update_and_draw(win)
    close_stars.update_and_draw(win)
    player.draw(win)
    player.update()
    pygame.display.update()

pygame.quit()