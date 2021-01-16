import pygame
from constants import colors

class Button:
    
    def __init__(self, screen, game_settings, msg):
        """
        Initialize button attributes
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 250, 50
        self.button_color = colors['green']
        self.text_color = colors['white']
        self.font = pygame.font.SysFont(None, 48)

        # Build the button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message should be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        Turns message into rendered image and center it on the button
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """
        Draw button on the screen
        """
        # Draws an empty button
        self.screen.fill(self.button_color, self.rect)

        # Renders message on the button
        self.screen.blit(self.msg_image, self.msg_image_rect)