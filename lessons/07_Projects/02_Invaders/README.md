# League Invaders


## 1 Background and player

Create a window that is the same size as the background, then add a player that can
can move left and right. When the space bar is pressed, make the player shoot a
bullet. Limit the number of bullets on the screen to 3. 

Your bullets should be added to a group, and when the bullet goes off the screen,
it should be removed from the group, using the `kill()` method.


## 2 Add a grid of enemies

Create a grid of enemies. All of the enemies should be sprites, and should be
added to an enemies group. 

Make the enemies move to the left and the right. Move the enemies by iterating
through their group, changing the x position of all enemies by a small amount.
While iterating, check that any enemies has hit the left or right side of the
screen, and if so, move all enemies down and change their direction.

## 3 Add collision detection

Check for collisions: 

* Between the enemies group and the bullets group. If a collision is detected,
  remove the enemy and the bullet from their respective groups.
* Between the enemies group and the player. If a collision is detected, end the
  game or decrement s life. 


## 4 Final Touches. 

* Add a scoring system.
* Add a Start Game and a Game Over screen.

