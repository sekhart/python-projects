import pygame

from pygame.sprite import Sprite


class Snake(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, sx_settings, screen):
        """Create a snake object at the center position."""
        super(Snake, self).__init__()
        self.screen = screen
        self.sx_settings = sx_settings
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, sx_settings.snake_width,
                                sx_settings.snake_height)

        self.screen_rect = screen.get_rect()
        # Start each new snake at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        # self.center = float(self.rect.centerx)

        self.color = sx_settings.snake_color
        self.speed_factor = sx_settings.snake_speed_factor

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self, sx_settings):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            print("----: " + str(self.rect))
            self.rect.centerx += self.sx_settings.snake_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.sx_settings.snake_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.sx_settings.snake_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.sx_settings.snake_speed_factor

        # Update rect object from self.center.
        # self.rect.centerx = self.center

    def draw_snake(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
