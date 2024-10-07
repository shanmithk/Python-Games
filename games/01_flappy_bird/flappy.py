import pygame

# Initialize Pygame
pygame.init()


from pathlib import Path
assets = Path(__file__).parent / 'assets'
background = pygame.image.load(assets/'background.png')


# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')


# Scale background to match the screen height
background_height = screen_height
background = pygame.transform.scale(background, (background.get_width(), screen_height))

# Get the dimensions of the background after scaling
background_width = background.get_width()

# Make an image the is the same size as the screen
image = pygame.Surface((screen_width, screen_height))

# Tile the background image in the x-direction
for x in range(0, screen_width, background_width):
    image.blit(background, (x, 0))
    


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Tile the background image in the x-direction
    for x in range(0, screen_width, background_width):
        screen.blit(background, (x, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
