from prettytable import PrettyTable

# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()



table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Shiggy", "Glumanda"])
table.add_column("Typ", ["Elektro", "Wasser", "Feuer"])
table.align = "l"
print(table)
