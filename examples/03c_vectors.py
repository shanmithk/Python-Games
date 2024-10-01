"""

Vector Jump

This programs demonstrates how to use vectors. When you hit SPACE, the
player will jump to the end of the green line. The left and right arrows
will rotate the green line, and the up and down arrows will change the
length of the green line.

"""
import pygame
import math

# Initialize Pygame
pygame.init()

# Settings class
class Settings:
    """A class to store all settings for the game."""
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PLAYER_SIZE = 20
    LINE_COLOR = (0, 255, 0)
    PLAYER_COLOR = (0, 0, 255)
    BACKGROUND_COLOR = (255, 255, 255)
    FPS = 60
    ANGLE_CHANGE = 3
    LENGTH_CHANGE = 5
    INITIAL_LENGTH = 100

# Initialize screen
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
pygame.display.set_caption("Player with Direction Vector")

# Clock to control frame rate
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self, x, y):
        """Initializes the Player with a position and direction vector.

        Args:
            x (int): The initial x-coordinate of the player.
            y (int): The initial y-coordinate of the player.
        """
        
        # We define two vectors, one for the position and one for the direction
        # The position vector is the current position of the player
        # The direction vector is the direction the player will move 
        
        self.position = pygame.math.Vector2(x, y)
        self.direction_vector = pygame.math.Vector2(Settings.INITIAL_LENGTH, 0)  # Initial direction vector

    
    def draw(self, show_line = True):
        """Draws the player and the direction vector on the screen."""
        # Draw player (as a square)
        pygame.draw.rect(screen, Settings.PLAYER_COLOR, (self.position.x - Settings.PLAYER_SIZE // 2, self.position.y - Settings.PLAYER_SIZE // 2, Settings.PLAYER_SIZE, Settings.PLAYER_SIZE))
        
        # Calculate the end point of the direction vector (line). Notice that we can just add the
        # direction vector to the position vector to get the end point.
        end_position = self.position + self.direction_vector
        
        # Draw direction vector (line)
        if show_line:
            # The drawing functions can take vectors as arguments
            pygame.draw.line(screen, Settings.LINE_COLOR, self.position, end_position, 2)
        

    def move(self):
        """Moves the player in the direction of the current angle."""
        
        init_position = self.position
        
        # Calculate the final position. You can just add the vectors!
        final_position = self.position + self.direction_vector
        
        #animate the movement
        length = self.direction_vector.length()
        N = int(length // 3)
        step = (final_position - self.position) / N
        for i in range(N):
            self.position += step
            
            screen.fill(Settings.BACKGROUND_COLOR)
            self.draw(show_line=False)
            pygame.draw.line(screen, Settings.LINE_COLOR, init_position, final_position, 2)
            pygame.display.flip()
            clock.tick(Settings.FPS)
            
def main():
    player = Player(Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2)
    running = True
    
    while running:
        screen.fill(Settings.BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        # Change the angle with left and right arrows
        

        if keys[pygame.K_LEFT]:
            player.direction_vector = player.direction_vector.rotate(-Settings.ANGLE_CHANGE)
        if keys[pygame.K_RIGHT]:
            player.direction_vector = player.direction_vector.rotate(Settings.ANGLE_CHANGE)
        
        # Change the length of the direction vector with up and down arrows
        if keys[pygame.K_UP]:
            player.direction_vector.scale_to_length(player.direction_vector.length() + Settings.LENGTH_CHANGE)
        
        if keys[pygame.K_DOWN]:
            new_length = max(10, player.direction_vector.length() - Settings.LENGTH_CHANGE)  # Prevent length from going below 10
            player.direction_vector.scale_to_length(new_length)
        
        # Move the player when spacebar is pressed
        
        if keys[pygame.K_SPACE]:
            player.move()
 
        # Draw the player and the direction vector
        player.draw()

        pygame.display.flip()
        clock.tick(Settings.FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
