import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Tank settings
TANK_SIZE = (40, 30)
BULLET_SIZE = (10, 5)
TANK_SPEED = 5
BULLET_SPEED = 7

# Sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
targets = pygame.sprite.Group()

class Tank(pygame.sprite.Sprite):
    def __init__(self, all_sprites: pygame.sprite.Group):
        super().__init__(all_sprites)
        self.image = pygame.Surface(TANK_SIZE)
        self.image.fill(GREEN)
        self.draw(self.image)
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.position = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2(1, 0)
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 5
            self.direction = self.direction.rotate(-5)
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
            self.direction = self.direction.rotate(5)
        if keys[pygame.K_UP]:
            self.position += self.direction * TANK_SPEED

        # Update tank position and rotation
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, surface):
        # Draw a triangle for the tank
        points = [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom)
        ]
        pygame.draw.polygon(surface, GREEN, points)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, all_sprites: pygame.sprite.Group, bullets: pygame.sprite.Group):
        super().__init__(all_sprites, bullets)
        self.image = pygame.Surface(BULLET_SIZE)
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.Vector2(position)
        self.direction = direction

    def update(self):
        self.position += self.direction * BULLET_SPEED
        self.rect.center = self.position

        # Remove bullet if it goes off screen
        if not screen.get_rect().contains(self.rect):
            self.kill()


class Target(pygame.sprite.Sprite):
    def __init__(self, position, all_sprites: pygame.sprite.Group , targets: pygame.sprite.Group):
        super().__init__(all_sprites, targets)
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=position)


# Function to create random targets
def create_random_targets(num_targets, all_sprites, targets):
    for _ in range(num_targets):
        x = random.randint(0, WIDTH - 30)
        y = random.randint(0, HEIGHT - 30)
        Target((x, y), all_sprites, targets)


# Create the tank
tank = Tank(all_sprites)
create_random_targets(10, all_sprites, targets)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a bullet
                Bullet(tank.position, tank.direction, all_sprites, bullets)

    # Update sprites
    all_sprites.update()

    # Check for bullet and target collisions
    for bullet in bullets:
        hit_targets = pygame.sprite.spritecollide(bullet, targets, True)
        if hit_targets:
            bullet.kill()

    # Drawing
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
