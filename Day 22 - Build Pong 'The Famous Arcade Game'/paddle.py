from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(x_pos, 0)

    def move_up(self):
        new_y_pos = self.ycor() + 20
        self.goto(self.xcor(), new_y_pos)

    def move_down(self):
        new_y_pos = self.ycor() - 20
        self.goto(self.xcor(), new_y_pos)