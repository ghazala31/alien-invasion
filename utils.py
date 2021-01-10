import sys

import pygame

def check_events(ship):
    """
    Responds to keypresses and mouse clicks
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)              


def check_keydown_events(event, ship):
    """
    Responds to keydown events
    """
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True


def check_keyup_events(event, ship):
    """
    Responds to keyup events
    """
    if event.key == pygame.K_RIGHT:
        # Stop moving the ship to the right
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        # Stop moving the ship to the left
        ship.moving_left = False  


def update_screen(screen, ship, game_settings):
    """
    Update images on the screen and flip to the new screen
    """
    # Fill the screen with the background color
    screen.fill(game_settings.bg_color)

    # Display the ship
    ship.blit()

    # Display the last drawn screen
    pygame.display.flip()