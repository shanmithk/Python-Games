# Python Games: Getting Started

Welcome to the second module of The LEAGUE's Python curriculum. This module is all about games, 
and it works a bit differently than the previous modules. Instead of learning a series of lessons, 
you will be building games using PyGame by reading and analysing existing Pygame programs. 

## Viewing Markdown Files

First things is that this curriculum will have many lesson files that will be in
the form of a README.md file. THe '.md' extension means "Markdown", which is a
way to format text. Its like a simple version of HTML. While you can read
Markdown files in a text editor, they are best viewed in a Markdown viewer. If
the first line of this file looks like 

    # Python Games: Getting Started

then you are reading this in a text editor, and you should open it in a Markdown
viewer.

To open the Markdown viewer, go to the file entry in the explorer window on the
left of the screen ( in VSCode, where it should be highlighed, because thats the
file you are reading now ) and right click to get the pop up menu. Then select
"Open Preview". This will open the file in the Markdown viewer.

The Markdown files will nearly always becalled "README.md" or "00_README.md",
but sometimes there will be markdown files with other names. 

## Reading Code

There will only be a few traditional lessons in this module, and they will be
short. Most of what you will learn will be from reading and analyzing code. This
is a very important skill for a programmer. Each lesson or assignment will be in
a directory with a README.md file that will explain what you need to do.

You will also need to read the Pygame documentation. You can find it at:

[https://www.pygame.org/docs/](https://www.pygame.org/docs/)

If you like extra help, you can also find many tutorials on the web. One of the best video tutorials
is [The Ultimate Introduction to PyGame](https://youtu.be/AY9MnQ4x3zk?si=HFtptJF9MVeq-hFO)


## Opening Your Virtual Screen

Since you will likely be working in a Codespace, you will need to open a virtual screen to run your Pygame programs.
To do this [floow these instuctions](https://curriculum.jointheleague.org/howto/python_codespaces.html#open-a-virtual-screen-on-the-web)

## Assignment

1. Copy `examples/01-move.py` into this directory.
2. Run the program and see what it does. Use the arrow keys to move the square around the screen.
3. Read the code and try to understand how it works.
4. Read the Pygame documentation for [pygame.draw](https://www.pygame.org/docs/ref/draw.html) and change the program to draw a circle. 
5. Read the documentation for [pygame.key](https://www.pygame.org/docs/ref/key.html) and change the program to move the circle with the `W`, `A`, `S`, and `D` keys.


## Important Tips

There are two ways to run a program. One is to use the  "Run" button at the top
of the screen. This will run the program in the terminal window at the bottom of
the screen. This will run the program in the terminal like a normal program. If
you do this, you will need to close the program clicking the close button on the
game window, or by hitting `Ctrl+C` in the terminal window.

The other way is by running with the debugger, which will give you more control.
Hit the F5 key to run the program with the debugger. The first time you do this
for a program, you will need to select an option from a window at the top of the
screen. 

When you run with the debugger, you can stop the program by hitting the red
square in the debugger window. Select the first option, "Python Debugger".  THen
you will get the debugger control window. You can use the buttons at the top of
the window to step through the program, or to stop it. The debugger window looks
like: 

![Debugger](https://images.jointheleague.org/vscode/debug_bar.png)

The red square will stop your program, and the creen reverse circle wil restart
it. The other buttons will let you step through the program.


