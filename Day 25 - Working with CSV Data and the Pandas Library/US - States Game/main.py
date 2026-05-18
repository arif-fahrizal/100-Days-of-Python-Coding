import turtle
import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.setup(725, 490)
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [ state for state in all_states if state not in guessed_state ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        txt = Turtle()
        txt.hideturtle()
        txt.penup()
        state_data = data[data.state == answer_state]
        txt.goto(state_data.x.item(), state_data.y.item())
        txt.write(answer_state)
        guessed_state.append(answer_state)