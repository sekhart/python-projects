import sys

import pygame

def check_events(sx_settings, screen):
    """event function"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def update_screen(sx_settings, screen):
    """ updating screen"""
    screen.fill(sx_settings.screen_bgcolor)
    # Make the most recently drawn screen visible
    pygame.display.flip()
    