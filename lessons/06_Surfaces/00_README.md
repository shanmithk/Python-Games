# Surfaces


Here is what the [Pygame Newbie Guide:](https://www.pygame.org/docs/tut/newbieguide.html) has to say about Surfaces:


    Know what a surface is.

    The most important part of pygame is the surface. Just think of a surface as a
    blank piece of paper. You can do a lot of things with a surface -- you can draw
    lines on it, fill parts of it with color, copy images to and from it, and set or
    read individual pixel colors on it. A surface can be any size (within reason)
    and you can have as many of them as you like (again, within reason). One surface
    is special -- the one you create with pygame.display.set_mode()Initialize a
    window or screen for display. This 'display surface' represents the screen;
    whatever you do to it will appear on the user's screen.

    So how do you create surfaces? As mentioned above, you create the special
    'display surface' with pygame.display.set_mode(). You can create a surface that
    contains an image by using pygame.image.load()load new image from a file (or
    file-like object), or you can make a surface that contains text with
    pygame.font.Font.render()draw text on a new Surface. You can even create a
    surface that contains nothing at all with pygame.Surface()pygame object for
    representing images.

    Most of the surface functions are not critical. Just learn Surface.blit(),
    Surface.fill(), Surface.set_at() and Surface.get_at(), and you'll be fine.


