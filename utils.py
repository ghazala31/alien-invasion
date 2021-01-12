import sys

import pygame

from bullet import Bullet

def check_events(screen, ship, bullets, game_settings):
    """
    Responds to keypresses and mouse clicks
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ship, bullets, game_settings)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)              


def check_keydown_events(event, screen, ship, bullets, game_settings):
    """
    Responds to keydown events
    """
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Fire bullet
        fire_bullet(screen, ship, bullets, game_settings)


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


def update_screen(screen, ship, bullets, game_settings):
    """
    Update images on the screen and flip to the new screen
    """
    # Fill the screen with the background color
    screen.fill(game_settings.bg_color)

    # Draw live bullets
    for bullet in bullets.sprites():
        bullet.draw()

    # Display the ship
    ship.blit()

    # Display the last drawn screen
    pygame.display.flip()


def update_bullets(bullets):
    """
    Updates positions of bullets and delete old ones
    """
    bullets.update()

    # Delete bullets that reach the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(screen, ship, bullets, game_settings):
    """
    Fire new bullet if the limit is not reached yet
    """
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(screen, ship, game_settings)
        bullets.add(new_bullet)