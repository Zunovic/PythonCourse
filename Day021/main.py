from turtle import Screen
import time
from score import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pysnake by Zunovic")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_state = True



while game_state:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision mit Food
    if snake.heading.distance(food) < 15:
        food.new_spot()
        snake.extend()
        scoreboard.increase_score()

    # Collision mit Wand
    if snake.heading.xcor() > 280 or snake.heading.xcor() < -280 or snake.heading.ycor() > 280 or snake.heading.ycor() < -280:
        game_state = False
        scoreboard.game_over()

    # Collision mit sich selbst
    # Egal an welcher Stelle sich der Kopf mit dem Rest überschneidet

    # Alle Segmente werden geprüft bis auf der Kopf. Sonst endet das Game sofort
    for segment in snake.segments[1:]:
        if snake.heading.distance(segment) < 10:
            game_state = False
            scoreboard.game_over()

screen.exitonclick()
