import pygame.font
from pygame.sprite import Group

from constants import colors
from ship import Ship

class Scoreboard:
    """Class to report scoring information"""

    def __init__(self, screen, game_settings, stats):
        """
        Initialize scorekeeping attributes
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = colors['black']
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """
        Turns the score into a rendered image
        """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.game_settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 20

    def prep_high_score(self):
        """
        Turns the high score into a rendered image
        """
        rounded_score = int(round(self.stats.high_score, -1))
        score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(score_str, True, self.text_color,
                                                 self.game_settings.bg_color)

        # Display the score at the top right of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """
        Turns the level into a rendered image
        """
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.game_settings.bg_color)

        # Display the score at the top right of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.screen_rect.bottom + 10

    def prep_ships(self):
        """
        Show how many ships (lives) are left
        """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.game_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """
        Draw score to the screen
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)