import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_events(screen, ship, bullets, aliens, button, game_settings, stats, sb):
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, ship, bullets, aliens, game_settings,
                              stats, sb, button, mouse_x, mouse_y)

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


def check_play_button(screen, ship, bullets, aliens, game_settings,
                      stats, sb, button, mouse_x, mouse_y):
    """
    Check if the play button is clicked
    """
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.game_active = True
        stats.reset_stats()
        game_settings.initialize_dynamic_settings()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        restart_game(screen, ship, bullets, aliens, game_settings)


def update_screen(screen, ship, bullets, aliens, button, game_settings, stats, sb):
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

    # Display score
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        button.draw()

    # Display the last drawn screen
    pygame.display.flip()


def update_bullets(screen, ship, bullets, aliens, game_settings, stats, sb):
    """
    Updates positions of bullets and delete old ones
    """
    bullets.update()

    # Delete bullets that reach the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(screen, ship, bullets, aliens, game_settings, stats, sb)

def update_aliens(screen, ship, bullets, aliens, game_settings, stats, sb):
    """
    Checks if the feet is at the edge then updates positions of aliens
    """
    check_fleet_edges(aliens, game_settings)
    aliens.update()

    # Check for alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, ship, bullets, aliens, game_settings, stats, sb)

    # Check for aliens hitting the bottom of the screen
    check_aliens_bottom(screen, ship, bullets, aliens, game_settings, stats, sb)

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


def get_number_of_rows(game_settings, alien_height, ship_height):
    """
    Determine the number of rows available to place the alien fleet
    """
    available_space_y = game_settings.screen_height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows


def create_alien(screen, aliens, alien_number, row_number, game_settings):
    """
    Creates one alien and place it in the row
    """
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(screen, ship, aliens, game_settings):
    """
    Create a fleet of aliens
    """
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    
    # Calcuate the number of aliens per row
    number_of_aliens_x = get_number_of_aliens_per_row(game_settings, alien_width)
    number_of_rows = get_number_of_rows(game_settings, alien_height, ship.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(screen, aliens, alien_number, row_number, game_settings)


def check_fleet_edges(aliens, game_settings):
    """
    Returns True if the fleet hits the right or left edges of the screen
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, game_settings)
            break


def change_fleet_direction(aliens, game_settings):
    """
    Drop the entire fleet and switch its direction
    """
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_bullet_alien_collision(screen, ship, bullets, aliens, game_settings,
                                 stats, sb):
    """
    Checks if there a collision between a bullet and an alien, and delete
    them accordingly
    """
    # Check for any bullets that have hit aliens and delete the bullet
    # and alien in every collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy existing bullets, increase speed and create new fleet
        bullets.empty()
        game_settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(screen, ship, aliens, game_settings)


def ship_hit(screen, ship, bullets, aliens, game_settings, stats, sb):
    """
    Respond to ship being hit by an alien
    """
    if stats.ships_left > 0:
        # Decrement number of ships left
        stats.ships_left -= 1
        sb.prep_ships()

        restart_game(screen, ship, bullets, aliens, game_settings)

        # Show mouse cursor
        pygame.mouse.set_visible(True)

        # Pause
        sleep(0.5)

    else:
        stats.game_active = False


def check_aliens_bottom(screen, ship, bullets, aliens, game_settings, stats, sb):
    """
    Check if any of the aliens reached the bottom of the screen
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(screen, ship, bullets, aliens, game_settings, stats, sb)
            break

        
def restart_game(screen, ship, bullets, aliens, game_settings):
    """
    Delete existing aliens and bullets, create a new fleet and recenter ship
    """
    # Delete aliens and bullets
    aliens.empty()
    bullets.empty()
    
    # Create new fleet and recenter ship
    create_fleet(screen, ship, aliens, game_settings)
    ship.center_ship()


def check_high_score(stats, sb):
    """
    Check if there is a new high score
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()