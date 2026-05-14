from turtle import Turtle, Screen
from prettytable import PrettyTable

# tinny = Turtle()
# ny_screen = Screen()
#
#
# tinny.shape("turtle")
# tinny.color("red")
# tinny.forward(100)
# print(ny_screen.canvwidth)
# ny_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'

print(table)