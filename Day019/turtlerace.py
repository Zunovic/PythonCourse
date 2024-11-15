import random
from turtle import Turtle, Screen


game_state = False
screen = Screen()
screen.setup(600, 500)
user_choice = screen.textinput("Wähl deine Farbe", "red, blue, orange, pink, purple, cyan")
color_picks = ["red", "blue", "orange", "pink", "purple", "cyan"]
positions = [-100, -70, -40, -10, 20, 50]
saved_racers = []

# Loop der die Turtles erstellt und an die Startlinie stellt
if user_choice:
    for turtle_start in range(0, 6):
        racer = Turtle(shape="turtle")
        racer.up()
        racer.color(color_picks[turtle_start])
        racer.goto(-290, positions[turtle_start])
        saved_racers.append(racer)
    game_state = True

# Loop der läuft bis, eine Turtle bei X 270 ist
while game_state:
    for racer in saved_racers:
        if racer.xcor() >= 270:
            game_state = False
            winner = racer.pencolor()
            if winner == user_choice:
                print(f"Du hast gewonnen! {winner} war als erstes im Ziel!")
            else:
                print(f"Du hast verloren! {winner} war als erstes im Ziel!")
#            print(racer.pencolor()) # debug
        move_dist = random.randint(0,10)
        racer.forward(move_dist)

screen.exitonclick()
