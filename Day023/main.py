import time
import random
from turtle import Screen
from player import Player
from car_spawn import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("Froscher Arcade Spiel")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
spawn_car = Car()

game_on = True

screen.listen()
screen.onkey(player.move_fd, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    spawn_car.move()

    if scoreboard.score < 12:
        random_chance = random.randint(1,  6)
    else:
        random_chance = random.randint(4, 6)

    if random_chance == 4:
        spawn_car.create_car()

    for car in spawn_car.car_handler:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 270:
        player.goto(0, -280)
        scoreboard.increase_score()
        spawn_car.level_up()

screen.exitonclick()