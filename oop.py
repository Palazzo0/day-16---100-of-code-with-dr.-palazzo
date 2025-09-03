# from turtle import Turtle, Screen
#
# palazzo = Turtle()
# # print(palazzo)
# palazzo.shape("turtle")
# palazzo.color("chocolate4")
# palazzo.forward(100)
# palazzo.left(120)
# palazzo.forward(100)
# palazzo.left(120)
# palazzo.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()
# # print(my_screen.canvheight)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Azurill", "Golduck"])
table.add_column("Type", ["Electric", "Fairy", "Water"])
table.align = "c"
print(table)