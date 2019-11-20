class Settings():
    """A class to store all settings for Snake Xenzia."""

    def __init__(self):
        """Initializing the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bgcolor = (230, 230, 230)

        # Bullet settings
        self.snake_speed_factor = 0.2
        self.snake_width = 7
        self.snake_height = 7

        self.snake_width_lr = 10
        self.snake_height_lr = 3

        self.snake_color = 60, 60, 60
        self.snakes_allowed = 1
        self.snake_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
