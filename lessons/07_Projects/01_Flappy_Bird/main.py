import pygame



import pygame
import random
from pathlib import Path

# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

    # Screen dimensions
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump")

    # Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# FPS
FPS = 60

    # Player attributes
PLAYER_SIZE = 25

player_speed = 5

# Obstacle attributes
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 20
obstacle_speed = 5

    # Font
font = pygame.font.SysFont(None, 36)
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.is_hovered = False

    def draw(self, screen, font):
        # Draw button rectangle
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=12)
        
        # Draw text
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Check if mouse is hovering over button
            self.is_hovered = self.rect.collidepoint(event.pos)
            self.current_color = self.hover_color if self.is_hovered else self.color

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False



# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(5,280)

        self.explosion = pygame.image.load(images_dir / "explosion1.gif")
        self.cactus = pygame.image.load(images_dir / "asteroid1.png")
        self.image = self.cactus
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rect.x -= obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()

    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load(images_dir / "background.png")
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.rect.width = WIDTH
        self.rect.height = HEIGHT
        self.image = pygame.transform.scale(self.image,(WIDTH, HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

class Projectile(pygame.sprite.Sprite):        
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLACK)  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.explosion = pygame.image.load(images_dir / "gameover.png")
        self.cactus = pygame.image.load(images_dir / "bluebird-upflap.png")
        self.image = self.cactus
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rect.x += obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()

    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLACK)
        self.dino = pygame.image.load(images_dir / "bluebird-midflap.")
        self.rect = self.image.get_rect()
        self.velocity = 0
        self.rect.x = 50
        self.rect.y = HEIGHT - PLAYER_SIZE - 10
        self.speed = player_speed
        self.image = self.dino
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect(center=self.rect.center)
        #self.image = pygame.transform.rotate(self.image,-90)
    def update(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            
             
            self.velocity = -3
        


        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.y += self.velocity
        self.velocity+= .2 
        # Keep the player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Create a player object
player = Player()
player_group = pygame.sprite.GroupSingle(player)

# Add obstacles periodically
def add_obstacle(obstacles):
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    
    if random.random() < 0.4:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        return 1
    return 0
def add_projectile(projectiles, x,y):
    """Creates and fires a projectile."""

    # new_projectile = Projectile(
    #     self.settings,
    #     position=self.rect.center,
    #     angle=self.angle,
    #     velocity=self.settings.projectile_speed,
        # )
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    
    

    projectile = Projectile(x,y)
    projectiles.add(projectile)
    


# Main game loop
def game_loop():
    button = Button(230,200,200,100,"retry",BLUE,RED)
    high_score = 0
    clock = pygame.time.Clock()
    game_over = False
    last_obstacle_time = pygame.time.get_ticks()
    projectiledelay = 0
    while True:
        # Group for obstacles
        obstacles = pygame.sprite.Group()
        projectiles = pygame.sprite.Group()
        playersprite = pygame.sprite.GroupSingle()
        player = Player()
        playersprite.add(player)
        backgroundsprite = pygame.sprite.GroupSingle()
        background = Background()
        backgroundsprite.add(background)
        obstacle_count = 0

        while not game_over:
            projectiledelay -= 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and projectiledelay <= 0:
                add_projectile(projectiles, player.rect.x, player.rect.y)
                projectiledelay = 50
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Update player
            player.update()

            # Add obstacles and update
            if pygame.time.get_ticks() - last_obstacle_time > 500:
                last_obstacle_time = pygame.time.get_ticks()
                obstacle_count += add_obstacle(obstacles)
            
            obstacles.update()
            projectiles.update()

            # Check for collisions
            collider = pygame.sprite.spritecollide(player, obstacles, dokill=False)
            for p in projectiles:
                collided=pygame.sprite.spritecollide(p, obstacles, dokill=False)
                for o in collided:
                    o.kill()
                    p.kill()
            if collider:
                collider[0].explode()
                game_over = True
                # pygame.kill()
            
            # Draw everything
            screen.fill(WHITE)
            backgroundsprite.draw(screen)
            playersprite.draw(screen)
            obstacles.draw(screen)
            projectiles.draw(screen)

            # Display obstacle count
            # obstacle_text = font.render(f"Obstacles: {obstacle_count}", True, BLACK)
            # screen.blit(obstacle_text, (10, 10))
            # if obstacle_count > high_score:
            #     high_score = obstacle_count
            # high_text = font.render(f"High Score: {high_score}", True, BLACK)
            # screen.blit(high_text, (400, 10))    
            
            
            pygame.display.update()
            clock.tick(FPS)


        # Game over screen
        
        while game_over == True:
            screen.fill(WHITE)
            retry_text = font.render("Game Over, try again", True, BLACK)
            screen.blit(retry_text, (10, 10))
            high_text = font.render(f"High Score: {high_score}", True, BLACK)
            screen.blit(high_text, (250, 100))
            #This is where i am adding the button
            
            for event in pygame.event.get():
                is_clicked = button.handle_event(event)
                if is_clicked:
                    game_over = False
            button.draw(screen, font)
            pygame.display.update()
if __name__ == "__main__":
    game_loop()