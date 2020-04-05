import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()
#############################################################
########### Method Parameters Description ###################
#############################################################
# Turtle None Creates and returns a new turtle object

# forward distance Moves the turtle forward

# backward distance Moves the turle backward

# right angle Turns the turtle clockwise

# left angle Turns the turtle counter clockwise

# up None Picks up the turtles tail

# down None Puts down the turtles tail

# color color name Changes the color of the turtle’s tail

# fillcolor color name Changes the color of the turtle will use to fill a polygon

# heading None Returns the current heading

# position None Returns the current position

# goto x,y Move the turtle to position x,y

# begin_fill None Remember the starting point for a filled polygon

# end_fill None Close the polygon and fill with the current fill color

# dot None Leave a dot at the current position

# stamp None Leaves an impression of a turtle shape at the current location

# shape shapename Should be ‘arrow’, ‘triangle’, ‘classic’, ‘turtle’, ‘circle’, or ‘square’

# speed integer 0 = no animation, fastest; 1 = slowest; 10 = very fast
