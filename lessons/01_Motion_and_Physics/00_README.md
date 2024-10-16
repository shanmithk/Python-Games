# Motion and Physics

<div style="border-left: 4px solid #3498db; padding: 10px;">
    <strong>Tip:</strong> <p>Don't forget to open the Markdown viewer to read this file!
     If the heading above looks like "# Motion and Physics" then you are not in the Markdown viewer.
Right-click on this file in the Explorer and select "Preview"</p>
</div><br/><br/>

Most of the games we will be writing have some physics, which is the motion of
objects in the game that should look realistic, like jumping or falling. Pygame
has some built in physics functions, but we will also need to write our own
physics code. The most basic physics are for moving objects around the screen,
so we will start there. 

## Basic Motion

Let's start with a simple program that moves a square around the screen, just to
see how it works. 

## Assignment 1

1. Open the program `01-move.py` 
2. Run the program and see what it does. Use the arrow keys to move the square
   around the screen.
3. Read the code and try to understand how it works.
4. Read the Pygame documentation for
   [pygame.draw](https://www.pygame.org/docs/ref/draw.html) and change the
   program to draw a circle for the player instead of a square.
5. Read the documentation for
   [pygame.key](https://www.pygame.org/docs/ref/key.html) and change the program
   to move the circle with the `W`, `A`, `S`, and `D` keys.

## Position, Velocity and Acceleration

Position is where a object is on the screen, and velocity is how fast it is
moving, also known as "speed". Because we are writing 2D games, our position and
speeds will have x and y components. That is, all of the motion of an object on
the screen can be described by its motion left and right, the x direction, and
up and down, the y direction.

Acceleration is a change in velocity, which is a change in speed or direction.
You accelerate when you go faster or slower. It doesn't look right if an object
just stops moving or starts moving full speed from a stop; to make it look
realistic, it has to speed up or slow down a bit at a time. 

Fortunately, this is really easy to do. Suppose we want to move our car to the right, 
which is the positive x direction. We can write a function that adds a little bit to the
x position each time it is called, and the car will move to the right. 

Let's start with no acceleration. This car just immedimmediately  starts moving at full speed, 
10 pixels each time step. 
```python

for i in range(100):
    car.x += 10
    
    car.draw()

```

Now, let's add some aceleration. We will add a little bit to the speed each time step. 
```python

acceleration = .1
for i in range(100):
    car.v += acceleration # Increase the speed by a little bit each time step
    car.x += velocity # Move the car by the speed each step
    
    car.draw()

```

That's it! We have a car that starts moving slowly and speeds up.

## Assignment 2

For assignment 2, read and then run `02_no_acceleration.py` in the
lessons directory, then `03_acceleration.py`. Notice that in the
program with acceleration, it seems like the red square is linked to the center
of the screen with a spring. Read the comments to understand how the programs
work and notice the difference in the motion. 

## Assignment 3

The most common game mechanic with acelleration is jumping. Let's look at
what it takes to make a player jump.

1. Open `04_gravity.py` 
2. Review your previous `01_move.py` program to study how keystrokes work in
   Pygame.
3. Change the `04_gravity.py` program so that instead of always jumping, the
   player jumps when the `space` key is pressed.
4. Change the program so that the player can jump higher by using the Control
   key along with the space. 

Bonus: 
* Ensure that the player can't jump while in the air.


Hints: 
* You might need to read the Pygame documentation for the
  [pygame.key](https://www.pygame.org/docs/ref/key.html) module to see how to
  read the keys.


## Motion in Two Dimensions and Collisions

If we were to allow our player to move left and right, we'd quickly have to
solve the problem of what happens when the player runs into a wall. This is a
collision, and it is a very important part of game. One simple way to handle a
collision is to just not let the player move into the wall, but a more realistic
way is to bounce the player off the wall.

Collisions with the edges of the screen are simple to detect: the player's position in x or y either
exceeds the screen size or goes below zero. Making the player bounce is also easy: just reverse the
velocity in the direction of the collision. 

```python
if player.x < 0 or player.x > screen_width:
    player.v.x = -player.v.x

if player.y < 0 or player.y > screen_height:
    player.v.y = -player.v.y
```

## Assignment 2

1. Copy `05_gravity_bounce.py` into this directory.
2. Change the program so that the player doesn't always jump. Instead, the player
   jumps only when the `space` key is pressed.
3. Change the program so that the player can jump to the left or right by pressing
   the `A` or `D` keys. You can pick any angle for the jump. 
4. Change the program so the player's velocity is reduced by a little bit each
   time step. ( aerodynamic wind drag ) When the player's x or y velocity is
   less than 0.1, set it to zero. This will make the player slow down and stop.
   If the Players velocity is zero, the player can jump again. The player
   shoud bounce off the ground.

Hints: 

* Jumping up will involve setting the y velocity, and jumping left or right
will also involve setting the x velocity.
* You can implement drag either by subtracting off a little bit of the velocity,
  but you will need to make sure the velocity doesn't go negative. Another way
   to do this is to multiply the velocity by a number less than 1, like 0.99.


## Next Steps

First, check in your code! You should check in ( commit ) and push your code
regularly. 

Second, don't forget about the [Pygame Documentation](https://www.pygame.org/docs/index.html). Your programs will
get better the more you know about Pygame.