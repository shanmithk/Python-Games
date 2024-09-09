"""
Gravity bounce with collision detection

Now we have a player that can jump and bounce off the sides of the screen.
Let's add an obstacle that the player must avoid. If the player hits the
obstacle, the player will bounce off of it, but you can have collisions
do other things, like end the game.

The important code in this program is the collisition detection:

    player.colliderect(obstacle)


"""
import pygame
from dataclasses import dataclass
from enum import Enum

#  When we define variables within the class, but not in a method, we call them
#  class variables. They are shared by all instances of the class, and we can access
#  them using the class name, like Colors.WHITE
class Colors:
    """Consants for Colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


class Game:
    """Main object for the top level of the game. Holds the main loop and other
    update, drawing and collision methods that operate on multiple other
    objects, like the player and obstacles."""
    
    def __init__(self, width: int = 500, height: int = 500, gravity: float = .3):

        pygame.init()

        self.running = True
        self.width = width
        self.height = height

        self.gravity = gravity

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def run(self):
        """Main game loop"""

        player = Player(self)

        while self.running:

            # Hitting a key or clicking the close buttonor hitting the ESC key
            # will generate an event that we can capture and use to end the game
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            player.update()

            self.screen.fill(Colors.WHITE)
            player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


class Player:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game, 
                 x: int = 100, y: int =  None,
                 v_y: float = 15,
                 width: int = 20, height: int = 20):
        
        self.game = game
        self.width = width
        self.height = height
      
        self.is_jumping = False
        self.v_jump = 15 # Jump velocity

        # Recalc Y since we don't know size in the default arg list. 
        y = y if y is not None else game.height - self.height

        self.x = x
        self.y = y

        self.v_y = v_y # Y Velocity

    def update(self):
        """Update player position, continuously jumping"""

        # Continuously jump.
        if self.is_jumping is False:
            # Jumping means that the player is going up. The top of the 
            # screen is y=0, and the bottom is y=SCREEN_HEIGHT. So, to go up,
            # we need to have a negative y velocity
            self.v_y = -self.v_jump
            self.is_jumping = True

        # Update player position. Gravity is always pulling the player down,
        # which is the positive y direction, so we add GRAVITY to the y velocity
        # to make the player go up more slowly. Eventually, the player will have
        # a positive y velocity, and gravity will pull the player down.

        self.v_y += self.game.gravity # Add gravity to the y velocity
        self.y += self.v_y # Update the player's y position, based on the current velocity

        # If the player hits the ground, stop the player from falling.
        # The player's position is measured from the top left corner, so the
        # bottom of the player is player.y + PLAYER_SIZE. If the bottom of the
        # player is greater than the height of the screen, the player is on the
        # ground. So, set the player's y position to the bottom of the screen
        # and stop the player from falling

        if self.y >= self.game.height - self.height:
            self.y = self.game.height  - self.height
            self.v_y = 0
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.BLACK, (self.x, self.y, self.width, self.height))


game = Game()
game.run()

