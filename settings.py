from constants import colors, MovingDirection

class Settings():
    """A class to store all the settings of the game"""
    
    def __init__(self):
        """
        Initializes the settings
        """
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = colors['light_gray']

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = colors['orange']
        self.bullets_allowed = 3

        # Aliens settings
        self.fleet_drop_speed = 10

        # Ship settings
        self.ship_limit = 3

        # How quickly the game scales up
        self.speedup_scale = 1.1

        # How quickly the alien points increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialize the settings that change throughout the game
        """
        self.ship_speed = 1
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = MovingDirection.RIGHT.value
        self.alien_points = 50

    def increase_speed(self):
        """
        Increase speed and alien points values
        """
        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.alien_speed += self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
