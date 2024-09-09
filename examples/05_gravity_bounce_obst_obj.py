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

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


class Game:

    running = True
    gravity = .3

    def __init__(self, width: int = 800, height: int = 600):
       
        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        pygame.display.flip()
        self.clock.tick(60)

    def draw(self, objs):
        # Draw everything
        self.screen.fill(Colors.WHITE)

        for obj in objs:
            obj.draw(self.screen)


class Player(pygame.Rect):

    is_jumping: bool = False

    v_jump: float = 15 # Jump velocity

    v_x: float = 0
    v_y: float = 0

    size: int = 0


    def __init__(self, game: Game, 
                 x: int = 100, y: int =  None,
                 v_x: float = 0, v_y: float = 15,
                 size: int = 20):
        
        self.game = game
        self.size = size
      
        # Recalc Y since we don't know size in the default arg list. 
        y = y if y is not None else game.height - size

        self.v_x = v_x # X Velocity
        self.v_y = v_y # Y Velocity

        # Where are self.x and self.y? They are in the Rect class, which is the
        # super class of the Player class.

        super().__init__(x, y, self.size, self.size)

    def jump(self):

        if self.is_jumping is False:
            self.v_y = -self.v_jump
            self.is_jumping = True

    def collide(self, obstacle):
        if self.colliderect(obstacle):
            self.v_y = -self.v_y

            # did the player hit the top or bottom of the obstacle?
            if self.y < obstacle.y:
                print("Player hit the top of the obstacle")


    def update(self):

        # Continuously jump.
        if self.is_jumping is False:
            # Jumping means that the player is going up. The top of the 
            # screen is y=0, and the bottom is y=SCREEN_HEIGHT. So, to go up,
            # we need to have a negative y velocity
            self.v_y = -self.v_jump
            self.is_jumping = True

        # If the player hits one side of the screen or the other, bounce the player
        if player.x <= 0 or player.x >= self.game.width - self.game.height:
            self.v_x = -self.v_x

        # If the player hits the top of the screen, bounce the player
        if player.y <= 0:
            self.v_y = -self.v_y


        # Update player position. Gravity is always pulling the player down,
        # which is the positive y direction, so we add GRAVITY to the y velocity
        # to make the player go up more slowly. Eventually, the player will have
        # a positive y velocity, and gravity will pull the player down.
        self.v_y += self.game.gravity
        player.y += self.v_y
        player.x += self.v_x

        # If the player hits the ground, stop the player from falling.
        # The player's position is measured from the top left corner, so the
        # bottom of the player is player.y + PLAYER_SIZE. If the bottom of the
        # player is greater than the height of the screen, the player is on the
        # ground. So, set the player's y position to the bottom of the screen
        # and stop the player from falling
        if self.y >= game.height - self.size:
            self.y = game.height  - self.size
            self.v_y = 0
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.BLACK, (self.x, self.y, self.size, self.size))

class Obstacle(pygame.Rect):

    def __init__(self, game: Game, width = 500, height = 10):
        self.game = game
        x  = (game.height - width) // 2 # Put the obstacle in the middle of the screen
        y  = (game.width - height) // 2

        super().__init__(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.RED, self)

game = Game()

player = Player(game)
obstacle = Obstacle(game)

while game.running:

    game.update()
    player.update()
    game.draw([player])

    #player.collide(obstacle)

pygame.quit()