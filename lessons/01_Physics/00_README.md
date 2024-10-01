# Physics

Most of the games we will be writing have some physics, which is the motion of objects in the
game that should look realistic, like jumping or falling. Pygame has some built in physics
functions, but we will also need to write our own physics code. THe most basic
physics are for moving objects around the screen, and we will start with that.

## Position, Velocity and Acceleration

Position is where a object is on the screen, and velocity is how fast it is moving. Because we 
are writing 2D games, our position and speeds will have x and y components. 

Accelleration is a change in velocity, which is a change in speed or direction.
You acellerate when you go faster or slower. It doesn't look right if an object
just stops moving or starts moving full speed from a stop; to make it look
realistic,  it has to speed up or slow down a bit at a time. 

Fortunately, this is really easy to do. Suppose we want to move our car to the right, 
which is the positive x direction. We can write a function that adds a little bit to the
x position each time it is called, and the car will move to the right. 


Let's start with no acelleration. This car just immedaitely starts moving at full speed, 
10 pixels each time step. 
```python

for i in range(100):
    car.x += 10
    
    car.draw()

```

Now, let's add some acelleration. We will add a little bit to the speed each time step. 
```python

acelleration = .1
for i in range(100):
    car.v += acelleration # Increase the speed by a little bit each time step
    car.x += velocity # Move the car by the speed each step
    
    car.draw()

```

That's it! We have a car that starts moving slowly and speeds up.


## Assignment 1

1. Copy `examples/02_gravity.py` into this directory.
2. Review your previous `01_move.py` program to studey how keystrokes work in Pygame.
3. Change the `02_gravity.py` program so that instead of always jumping, the
   player jumps when the `space` key is pressed.
4. Change the program so that the player can jump higher by using the Control
   key along with the space. 

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

1. Copy `examples/03a_gravity_bounce.py` into this directory.
2. Change the program so that the player doesn't always jump. Instead, the player
   jumps when the `space` key is pressed.
3. Change the program so that the player can jump to the left or right by pressing
   the `A` or `D` keys.
4. Change the program so the player's velocity is reduced by a little bit each
   time step. ( areodynamic wind drag ) When the player's x or y velocity is
   less than 0.1, set it to zero. This will make the player slow down and stop.
   IF the Players velocity is zero, the player can jump again. 



