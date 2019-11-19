import sys

import pygame

from settings import Settings

import game_business as gb



def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    
    sx_settings = Settings()
    
    screen = pygame.display.set_mode((sx_settings.screen_width,sx_settings.screen_height))
    pygame.display.set_caption('Snake Xenzia')
       
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gb.check_events(sx_settings, screen)
        gb.update_screen(sx_settings, screen)
    
    
run_game()

