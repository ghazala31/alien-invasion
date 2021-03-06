import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """A class representing the ship"""

    def __init__(self, screen, game_settings):
        """
        Initializes the ship
        """
        super().__init__()
        
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship's image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Initialize the ship in the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)

        # Initialize moving flags
        self.moving_right = False
        self.moving_left = False

    def blit(self):
        """
        Draws the ship at its current location
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Updates the ship's location
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        """
        Center the ship on the screen
        """
        self.center = self.screen_rect.centerx