# This is our basic snake game.
# We will utilise python and some libraries to make it

import turtle # this imports the turtle to be used in our game.

t = turtle.Turtle()

for c in [ 'green', 'blue', 'red', 'white']:
    t .color(c)
    t.forward(50)
    t. left(75)

