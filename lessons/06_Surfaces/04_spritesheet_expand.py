"""Display a spritesheet expanded to a larger size.

"""

import pygame
from pathlib import Path
from spritesheet import SpriteSheet

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("SpriteSheet Test")

# Load the sprite sheet
images = Path(__file__).parent / 'images'
filename = images / 'spritesheet.png'  # Replace with your actual file
cellsize = (16, 16)  # Replace with your sprite's cell size (width, height)

if not filename.exists():
    raise FileNotFoundError(f"Error: The file {filename} does not exist.")


# Create a SpriteSheet instance
spritesheet = SpriteSheet(filename, cellsize)
print(spritesheet)

# Load a single sprite at index (0, 0)
sprite = spritesheet.image_at((0, 0), colorkey=-1)

# Load a strip of 3 sprites starting at (1, 0)
sprite_strip = spritesheet.load_strip(1, 3, colorkey=-1)

def sprite_pos(index):
    """Returns the screen position of a sprite index, where we will draw the sprite"""

    # Cell size on the screen
    cell_x = spritesheet.cellsize[0]*2+20
    cell_y = spritesheet.cellsize[1]*2+20

    # Number of cells that fit on the screen in x
    cols = screen_width // cell_x

    row, col = divmod(index, cols) # equivalent to row = index // cols, col = index % cols

    x = col * cell_x + 20
    y = row * cell_y + 20
    
    print(x, y) 
    return x, y
    
    
def draw_sprite(sprite, index):
    x, y = sprite_pos(index)
    screen.blit(sprite, (x, y))
    
def text_pos(index):
    x,y = sprite_pos(index)
    return x, y + spritesheet.cellsize[1]*2 + 3


def draw_text(text, index):
    x, y = text_pos(index)
    font = pygame.font.Font(None, 20)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))
    
screen.fill((0, 0, 0))  # Clear screen with black


# Iterate through all of the sprites displaying the sprite and the sprite's index
for i in range(spritesheet.num_sprites):
    sprite = spritesheet.image_at(i, colorkey=-1)
    sprite = pygame.transform.scale(sprite, (spritesheet.cellsize[0] * 2, spritesheet.cellsize[1] * 2))
    
    draw_sprite(sprite, i)
    draw_text(str(i), i)



running = True
while running:

    pygame.display.flip()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

