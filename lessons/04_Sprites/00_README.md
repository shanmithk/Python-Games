# Sprites

A "Sprite" is a 2D image that is used to represent an object in a game. Sprites
can be static images or animated sequences. In this lesson, we will learn how to
create and use sprites in Pygame. The name "Sprite" comes from the early days of
computer graphics when a sprite was a small, movable object that could be placed
anywhere on the screen, floating above the background like a mythological
spirit.

In PyGame a sprite is a class that represents a game object that has an image, 
position, and other properties. Pygame provides a `Sprite` class that we can use
to create our own sprite classes. We can also use the `Sprite` class to create
groups of sprites that we can update and draw all at once.

The important parts of Sprites are: 

* **Image**: The image that represents the sprite.
* **Rect**: The rectangle that defines the position and size of the sprite.
* **Group**: A collection of sprites that can be updated and drawn together.

In this lesson we will compare two program, one that uses a sprite and one that
does not. 

## Program 1: No Sprite

Our first program is Object Oriented, but does not use Sprites. Open and
run `examples/05a_boring_asteroids.py`. The left and right arrows will turn the 
ship, and the space bar will fire a bullet.

Here is our code for the spaceship:

```python
    def __init__(self, settings):
        self.settings = settings
        self.position = pygame.Vector2(self.settings.width // 2, self.settings.height // 2)
        self.angle = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 5
        if keys[pygame.K_RIGHT]:
            self.angle += 5

    def draw(self, surface):
        points = [
            pygame.Vector2(0, -self.settings.triangle_size),  # top point
            pygame.Vector2(-self.settings.triangle_size / 2, self.settings.triangle_size),  # left side point
            pygame.Vector2(self.settings.triangle_size / 2, self.settings.triangle_size)  # right side point
        ]
        rotated_points = [point.rotate(self.angle) + self.position for point in points]
        pygame.draw.polygon(surface, self.settings.colors['white'], rotated_points)

```

In this code, the `draw()` method of the `Spaceship` class draws the spaceship every frame.

The main loop is in the `Game` object, and it looks like this:

```python
 class Game:

    def draw(self):
        self.screen.fill(self.settings.colors['black'])
        self.spaceship.draw(self.screen)
        for projectile in self.projectiles:
            projectile.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.settings.fps)
        pygame.quit()

```

When we `run()` the game, the `Game.draw()` method will draw the spaceship and
the projectiles. The `Spaceship.draw()` method will draw the spaceship as a
triangle.

You should review the code in `examples/05a_boring_asteroids.py` to see how the
spaceship and projectiles are created and updated.

## Program 2: Using Sprites

Now look at `examples/05b_boring_asteroids_sprite.py`. This program uses a `Sprite` class to
represent the spaceship and the projectiles. The `Sprite` class is a subclass of
`pygame.sprite.Sprite` and has an `image` and a `rect` attribute. The `image`
attribute is the image that represents the sprite, and the `rect` attribute is a
rectangle that defines the position and size of the sprite.

Here is what the main part of the `Spaceship` class looks like:

```python

class Spaceship(pygame.sprite.Sprite):
    """Class representing the spaceship."""

    def __init__(self, settings, position):
        super().__init__()

        ...

        self.angle = 0
        self.original_image = self.create_spaceship_image()

        # For Sprites, the image and rect attributes are part of the Sprite class
        # and are important. The image is the surface that will be drawn on the screen

        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)

        ...

```

The `Spaceship` class is a subclass of `pygame.sprite.Sprite`, so it inherits some of the
properties of the `Sprite` class. The `image` and `rect` attributes are part of
the `Sprite` class, and are used to draw the sprite on the screen.

One important difference is that `Spaceship` does not have `draw()` method. Instead, Pygame will 
draw it for us when we add it to a sprite group.

Here are the important parts of the `Game`  class:


```python

class Game:
    """Class to manage the game loop and objects."""

    def __init__(self, settings):
        self.all_sprites = pygame.sprite.Group()

    def add(self, sprite):

        self.all_sprites.add(sprite)

    ...

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.all_sprites.draw(self.screen)
```


When we start the game, we `.add()` the spaceship and the projectiles to the
`all_sprites` group. The `all_sprites` group is a `pygame.sprite.Group` that
contains all the sprites in the game. We can update and draw all the sprites in
the group at once.

So, when we call `self.all_sprites.update()`, the `update()` method of each
sprite in the group is called. When we call `self.all_sprites.draw(self.screen)`,
the `draw()` method of each sprite in the group is called. That's why there is no
need to call the `draw()` method of the spaceship and the projectiles in the
`Game` class; all of that is handled by the sprite group.

## Assignment 1

1. Copy the `examples/05b_boring_asteroids_sprite.py` program to a new file in
   this directoty.
2. Modify the `Spaceship` class so that the spaceship can move forward when the
   up arrow key is pressed. The spaceship should move in the direction it is
   facing. You can use the `pygame.Vector2` class to represent the position and
   velocity of the spaceship.


For (2), you will need to add a `velocity` attribute to the `Spaceship` class. Review
past programs for clues. 

Make seperate functions for each of the things you are updating in your spaceship. For instance, your
`update()` method might look like this:

```python
    def update(self):
        
        self.handle_input()
        self.update_angle()
        self.update_position()

        super().update() # Don't for get this part!
```

## Assignment 2

Add some images to the spaceship and the projectiles. 


1. First set the assets directory, in code at the top of your file.

```python
from pathlib import Path


assets = Path(__file__).parent.parent.parent / "examples" / "assets"

```

2. Create a subclass of Spaceship that will load an image for the spaceship. 

```python
class AlienSpaceship(Spaceship):
    
    def create_spaceship_image(self):
        """Creates the spaceship shape as a surface."""
        
        return pygame.image.load(assets/'alien1.gif')
        
```

3. In the end of the file, create a new instance of the AlienSpaceship class, instead of the Spaceship class. 
4. Run the program. 

You spaceship should have turned from a triangle to a flying saucer! The
`AlienSpaceship` class is a subclass of the `Spaceship` class, so it inherits
all the methods and attributes of the `Spaceship` class. The only difference is
that the `create_spaceship_image()` method is overridden to load an image from a
file.   It's like we copied the `Spaceship` class and changed only the
`create_spaceship_image()` method.
