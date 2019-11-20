import game_business as gb
import pygame
from pygame.sprite import Group
from settings import Settings
from snake import Snake


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()

    sx_settings = Settings()

    screen = pygame.display.set_mode((sx_settings.screen_width, sx_settings.screen_height))
    pygame.display.set_caption('Snake Xenzia')

    snake = Snake(sx_settings, screen)
    snakes = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gb.check_events(sx_settings, screen, snake, snakes)
        snake.update(sx_settings)
        gb.update_screen(sx_settings, screen, snake, snakes)


run_game()
