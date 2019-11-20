import sys

import pygame


def check_events(sx_settings, screen, snake, snakes):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicked...')
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sx_settings, screen, snake, snakes)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, snake)


def check_keydown_events(event, sx_settings, screen, snake, snakes):
    """Respond to keydown."""
    if event.key == pygame.K_RIGHT:
        snake.moving_right = True
    elif event.key == pygame.K_LEFT:
        snake.moving_left = True
    elif event.key == pygame.K_UP:
        snake.moving_up = True
    elif event.key == pygame.K_DOWN:
        snake.moving_down = True
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, snake):
    """Respond to keyup."""
    if event.key == pygame.K_RIGHT:
        snake.moving_right = False
    elif event.key == pygame.K_LEFT:
        snake.moving_left = False
    elif event.key == pygame.K_UP:
        snake.moving_up = False
    elif event.key == pygame.K_DOWN:
        snake.moving_down = False


def check_fleet_edges(ai_settings, snakes):
    """Respond appropriately if any snakes have reached an edge."""
    print("checking edges---------")
    for snake in snakes.sprites():
        print('---' + str(snake))
        if snake.check_edges():
            change_fleet_direction(ai_settings, snakes)
            break


def change_fleet_direction(ai_settings, snakes):
    """Drop the entire fleet and change the fleet's direction."""
    print("----------------------")
    for snake in snakes.sprites():
        snake.rect.y += sx_settings.fleet_drop_speed
        sx_settings.fleet_direction *= -1


def update_screen(sx_settings, screen, snake, snakes):
    """ updating screen"""
    screen.fill(sx_settings.screen_bgcolor)
    # Make the most recently drawn screen visible
    snake.draw_snake()
    pygame.display.flip()
