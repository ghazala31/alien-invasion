import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from utils import (check_events, update_screen, update_bullets,
                   update_aliens, create_fleet)

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

    # Create bullets group
    bullets = Group()

    # Create aliens group
    aliens = Group()

    # Create the fleet of aliens
    create_fleet(screen, ship, aliens, game_settings)

    # Main loop of the game
    while True:
        check_events(screen, ship, bullets, game_settings)
        ship.update()
        update_bullets(screen, ship, bullets, aliens, game_settings)
        update_aliens(aliens, game_settings)
        update_screen(screen, ship, bullets, aliens, game_settings)


run_game()