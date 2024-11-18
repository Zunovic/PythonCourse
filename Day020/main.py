from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pysnake by Zunovic")
snake = Snake()
game_state = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while game_state:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
