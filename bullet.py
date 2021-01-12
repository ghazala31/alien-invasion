import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class representing bullets fired from the ship"""

    def __init__(self, screen, ship, game_settings):
        """
        Creates a bullet object at the ship's current position
        """

        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed = game_settings.bullet_speed

    def update(self):
        """
        Move the bullet up the screen
        """
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        """
        Draw bullet on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
    