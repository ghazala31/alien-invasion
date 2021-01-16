import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, screen, game_settings):
        super().__init__()

        self.screen = screen
        self.game_settings = game_settings

        # Load the alien image and set its rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blit(self):
        """Draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Move the alien to the right or to the left
        """
        self.x += (self.game_settings.alien_speed * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        Returns True if an alien is at the edge of the screen
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True
