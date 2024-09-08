"""
Dino Jump Game

This program will show you a simple display with a player that just when the
space key is pressed, it jumps. But, it isn't a very good jump, so we'll have to
make it better later. 

"""
import pygame
import random

# Initialize Pygame. Nothing works if you don't do this!
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
PLAYER_SIZE = 50
GRAVITY = 1
JUMP_DURATION = 50

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define player
player = pygame.Rect(100, SCREEN_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)


running = True
clock = pygame.time.Clock()
jump_counter = 0

while running: # Main loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # Get all of the keystrokes
    keys = pygame.key.get_pressed()

    # If the space key is pressed, the player jumps. 
    # Search for 'pygame.K_SPACE' in the Pygame documentation to see what other
    # keys you can use. ( https://www.pygame.org/docs/ )
    if keys[pygame.K_SPACE] and  jump_counter == 0:
        jump_counter = JUMP_DURATION

    if jump_counter > 0: # Bring the player back down. 
        jump_counter -= 1

    # Set the players position
    player.y = SCREEN_HEIGHT - PLAYER_SIZE - jump_counter

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)

    pygame.display.flip() # Update the screen

    # Limit the game to 30 frames per second. This will make the game run more
    # smoothly on most computers
    clock.tick(30)

pygame.quit()
