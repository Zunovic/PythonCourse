from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pysnake by Zunovic")
snake_squares = []
start_pos = (0, -20, -40)
game_state = True

for i in range(len(start_pos)):
    square = Turtle("square")
    square.color("white")
    square.up()
    square.goto(start_pos[i], 0)
    screen.update()
    snake_squares.append(square)

while game_state:
    screen.update()
    time.sleep(0.1)

# Snake bleibt verbunden und die einzelnen Segmente nehmen den Platz vom vorgänger ein
    for piece_num in range(len(snake_squares) - 1, 0, -1):
        new_x = snake_squares[piece_num - 1].xcor()
        new_y = snake_squares[piece_num - 1].ycor()
        snake_squares[piece_num].goto(new_x, new_y)
    snake_squares[0].forward(20)
    snake_squares[0].left(90)

screen.exitonclick()
