import pygame
from helpers import colors, physics
from .player import Player
from .stars import Stars
from .pipe import Pipe


"""
this is for full screen. However objects need to be adjusted to 
current screen size which is not supported at the moment
screen_width, screen_height = (
    pygame.display.Info().current_w,
    pygame.display.Info().current_h,
)
"""
pygame.init()
print(
    (
        pygame.display.Info().current_w,
        pygame.display.Info().current_h,
    )
)

screen_width, screen_height = 1080, 720

font = pygame.font.SysFont("ubuntu-mono", 35, True, False)
font_big = pygame.font.SysFont("ubuntu-mono", 70, True, False)


class Game(object):
    def __init__(self):
        self.win = pygame.display.set_mode((screen_width, screen_height))

        self.pipe_gap = 350
        self.pipe_width = 100
        self.n_pipes = 2

        self.stars = []
        self.star_layers = 10
        for i in range(self.star_layers):
            self.stars.append(
                Stars(
                    surface=self.win,
                    star_count=int(1000 / self.star_layers),
                    star_movement=[-(2 + 2 * i / (self.star_layers)), 0],
                    star_size=2 + i * 2 / self.star_layers,
                )
            )

        self.clock_ticks = 0
        self.highscore = 0

    def init_game(self):
        self.points = 0
        self.is_main_loop = True
        self.collided = False
        self.player = Player(self.win)
        self.pipes = [
            Pipe(surface=self.win, pipe_gap=self.pipe_gap, pipe_width=self.pipe_width)
            for i in range(self.n_pipes)
        ]

        for i in range(self.n_pipes):
            self.pipes[i].rect1.x += i * (screen_width + 100) / (self.n_pipes)
            self.pipes[i].rect2.x += i * (screen_width + 100) / (self.n_pipes)

    def main_loop(self):
        self.win.fill(colors.BACKGROUND)

        for star_layer in self.stars:
            star_layer.update_and_draw(self.win)
            star_layer.star_movement = [
                star_layer.star_movement[0],
                self.player.vel_y * 0.005 * star_layer.size,
            ]

        for pipe in self.pipes:
            pipe.update_and_draw(self.win)
            if physics.check_collision(self.player, pipe):
                self.collided = True

            if pipe.rect1.x < 0 - pipe.width:
                if self.pipe_gap > 130:
                    self.pipe_gap -= 5
                if self.pipe_width > 10:
                    self.pipe_width -= 1.5

                pipe.reset(self.win, self.pipe_gap, self.pipe_width)

        self.points += (pygame.time.get_ticks() - self.clock_ticks) / 100000

        self.player.draw(self.win)

        text = font.render(f"points: {int(self.points)}", 5, (255, 255, 255))
        self.win.blit(text, (10, 10))

        self.player.update()
        pygame.display.update()

    def final_screen(self):
        self.win.fill(colors.BACKGROUND)

        for star_layer in self.stars:
            star_layer.update_and_draw(self.win)
            star_layer.star_movement = [
                star_layer.star_movement[0],
                0,
            ]

        texts = []
        texts.append(
            font_big.render(f"Final points: {int(self.points)}", 5, (255, 255, 255))
        )
        texts.append(
            font_big.render(f"Highscore: {int(self.highscore)}", 5, (255, 255, 255))
        )
        texts.append(font.render("Press R to restart", 5, (255, 255, 255)))

        text_rect = texts[0].get_rect(center=(screen_width / 2, screen_height / 2))

        for i in range(len(texts)):
            self.win.blit(texts[i], text_rect.move((0, 100 * (i - len(texts) / 2))))
        pygame.display.update()
