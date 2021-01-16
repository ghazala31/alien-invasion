import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
from utils import (check_events, update_screen, update_bullets,
                   update_aliens, create_fleet)

def run_game():
    """
    Main function that runs the game
    """
    # Initialize the game and create the screen
    pygame.init()
    game_settings = Settings()
    stats = GameStats(game_settings)

    screen = pygame.display.set_mode((game_settings.screen_width,
                                      game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create the play button
    button = Button(screen, game_settings, "Start the game")
    
    # Create score board
    sb = Scoreboard(screen, game_settings, stats)

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
        check_events(screen, ship, bullets, aliens, button, game_settings, stats, sb)

        if stats.game_active:
            ship.update()
            update_bullets(screen, ship, bullets, aliens, game_settings, stats, sb)
            update_aliens(screen, ship,  bullets, aliens, game_settings, stats, sb)
        update_screen(screen, ship, bullets, aliens, button, game_settings, stats, sb)


run_game()