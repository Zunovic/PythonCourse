from turtle import Screen
from window import Paddle, Ball, Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong recreation by Zunovic")
screen.tracer(0)


right_paddle = Paddle()
right_paddle.set_cords(1)
left_paddle = Paddle()
left_paddle.set_cords(0)

score = Scoreboard()
ball = Ball()

screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_loop = True


while game_loop:
    time.sleep(.1)
    screen.update()
    ball.move()

    # Game logic
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(left_paddle) <50 and ball.xcor() < -320):
        ball.bounce_x()
        score.increase_score()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
        score.game_over()
        game_loop = False

screen.exitonclick()




