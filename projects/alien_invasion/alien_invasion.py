import game_functions as gf
import pygame
from alien import Alien
from button import Button
from game_stats import GameStats

from pygame.sprite import Group
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


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

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            bullets.update()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
