import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class BarrierManager:

    def __init__(self):
        self.barriers = []
        self.barrier_speed = STARTING_MOVE_DISTANCE

    def create_barrier(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            barrier = Turtle("square")
            barrier.shapesize(1, 2)
            barrier.penup()
            barrier.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            barrier.goto(300, random_y)
            self.barriers.append(barrier)

    def move_barriers(self):
        for barrier in self.barriers:
            barrier.backward(self.barrier_speed)

    def level_up(self):
        self.barrier_speed += MOVE_INCREMENT