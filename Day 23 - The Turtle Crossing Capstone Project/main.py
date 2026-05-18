import time
from turtle import Screen
from player import Player
from barrier_manager import BarrierManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


player = Player()
barrier_manager = BarrierManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    barrier_manager.create_barrier()
    barrier_manager.move_barriers()

    # Detect collision with barrier
    for barrier in barrier_manager.barriers:
        if barrier.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful
    if player.finish():
        player.start_again()
        barrier_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()