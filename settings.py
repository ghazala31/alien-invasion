from colors import colors

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
        self.ship_speed = 1.5  # pixels per key press