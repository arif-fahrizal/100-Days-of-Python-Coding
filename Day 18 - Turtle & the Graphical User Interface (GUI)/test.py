from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
colormode(255)

# Square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# Dashed Line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

directions = [0,90,180,270]
turtle.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    colours = (r, g, b)

    return colours

def draw_shape(side):
    for _ in range(side):
        turtle.forward(100)
        turtle.right(360 / side)

def random_walk():
    for _ in range(200):
        turtle.color(random_color())
        turtle.forward(30)
        turtle.setheading(random.choice(directions))

def spirograph(gap):
    for _ in range(int(360 / gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)

# Draw Shape
# for shape_side in range(3,11):
#     turtle.color(random.choice(colours))
#     draw_shape(shape_side)

# Random Walk
# random_walk()

# Spirograph
spirograph(5)



screen = Screen()
screen.exitonclick()