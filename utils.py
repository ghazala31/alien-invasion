import sys

import pygame

from bullet import Bullet
from alien import Alien

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

    elif event.key == pygame.K_q:
        # Exit the game
        sys.exit()


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


def update_screen(screen, ship, bullets, aliens, game_settings):
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

    # Display the alien
    aliens.draw(screen)

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


def get_number_of_aliens_per_row(game_settings, alien_width):
    """
    Determine the number of aliens that fit in one row
    """
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))
    return number_of_aliens_x


def create_alien(screen, aliens, alien_number, game_settings):
    """
    Creates one alien and place it in the row
    """
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(screen, aliens, game_settings):
    """
    Create a fleet of aliens
    """
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    
    # Calcuate the number of aliens per row
    number_of_aliens_x = get_number_of_aliens_per_row(game_settings, alien_width)

    # Create the first row of aliens
    for alien_number in range(number_of_aliens_x):
        create_alien(screen, aliens, alien_number, game_settings)