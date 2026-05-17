import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500,400)
user_choice = screen.textinput("Make your choice", "Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_pos = [80, 50, 20, -10, -40, -70]
all_turtles = []
is_race_on = False

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)







screen.exitonclick()