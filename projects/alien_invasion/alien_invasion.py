import sys

import pygame

from settings import Settings

from ship import Ship

from alien import Alien

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))    
    pygame.display.set_caption("Alien Invasion")
        
    # Make a ship
    ship = Ship(ai_settings, screen)
    
    # Make an alien
    alien = Alien(ai_settings, screen)
    
    # Make a ship, a group of bullets, and a group of aliens.
    bullets = Group()    
    aliens = Group()
       
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            bullets.update()
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)        
        
run_game()