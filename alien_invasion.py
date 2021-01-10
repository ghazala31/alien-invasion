import sys

import pygame

from colors import colors
from settings import Settings
from ship import Ship
from utils import check_events, update_screen

def run_game():
    """
    Main function that runs the game
    """
    # Initialize the game and create the screen
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width,
                                      game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create the ship
    ship = Ship(screen, game_settings)

    # Main loop of the game
    while True:
        check_events(ship)
        ship.update()
        update_screen(screen, ship, game_settings)

run_game()