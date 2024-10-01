# Vector Example Program

The program `examples/03c_vectors.py` is a simple program that demonstrates how
to use vectors to move an object around the screen.

![Vector Example](images/vector_example.png)


You can move the green line around the player with the left and right arrow
keys. The up and down arrow keys will make the line longer or shorter. When you
hit the space bar, the player will move along the green line to the new
position.

In this program, both the line and the player are represented with a vector. Read the
program to see how we use vectors to move the player along the line.


## Gravity Bounce Update

The program `examples/03d_gravity_bounce_vec.py` is an update to the gravity
bounce program that uses vectors to represent the player's position and
velocity.


## Assignment 1

1. Copy `examples/03d_gravity_bounce_vec.py` into this directory.
2. Add drag to the program, like we did in a earlier assignment, but use a
   vector to represent the drag. Subtract the drag vector from the player's
   velocity each time step to make the player slow down. 

Your drag can be configured with a scalar value ( a float ) is turned into a
vectorin the Payer class initializer, or in the Game class.  Be sure to use the
drag vector to modify the player's velocity in the appropriate method. 

If you want a more sophisticated, realistic drag, you can make the drag vector
proportional to the square of the player's velocity. This is a simple model of
air resistance, which is proportional to the square of the velocity.


## Assignment 2

Now we are going to add thrust to the player. The player will have a thrust
vector that will be added to the player's velocity when the player presses the
space bar. This will work just like the drag vector, except you will add the
thrust vector instead of subtract it, and you will add the thrust vector only
when the player jumps, rather than subtracting a little bit every time step. 

1. Add a thrust vector to the player class. for now, just make the the thrust
   vector point up. 
2. Remove the logic that causes continuoys jumping. After the player touches the
   ground, the player should stop and not bounce. 
3. Add a method to the Player, `update_input(self)` that will read the keys.
   Call this method along with the other update functions in `update()` If the
   player presses the space bar, add the thrust vector to the player's velocity.
   Read the code in `examples/03c_vectors.py` to see how get the keys.

### Things to try

* Change the direction of the thrust vector. You might have the vector point
  straight up, so the player can only jump up, but you can change the direction
  to the player jumps in a different direction. Make the player jump sideways.

## Assignment 3

Let's update the program to allow the user to jump in any direction. For this,
we will use the example from   `examples/03c_vectors.py`. In the example
program, the player moves along the green line when the space bar is pressed.
Instead of moving along the line, we will add a thrust vector to the player's
velocity when the space bar is pressed. Adding thrust will work just like drag,
except that you will add the thrust vector to the player's velocity instead of
subtracting it.

1. Add a line that represents the thrust vector, which you will draw on the
   screen to show the player which way they are jumping, just like in the
   `03c_vectors.py` example.
2. Update your `update_input()` method to read the arrow keys and adjust the
   thrust vector. You can use the left and right arrow keys to change the
   direction of the thrust vector, and the up and down arrow keys to change the
   length of the thrust vector. Review the code in `03c_vectors.py` for hints.


### Things to try

Does your thrust vector line look right? Does it start drawing from the center of the player? Is
it long enough to see? Is it the right color? You might have to adjust the starting point, 
and increase the length of the line to make it visible.

