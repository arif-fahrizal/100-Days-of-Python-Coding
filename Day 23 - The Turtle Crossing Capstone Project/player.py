from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.start_again()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        return self.ycor() > FINISH_LINE_Y