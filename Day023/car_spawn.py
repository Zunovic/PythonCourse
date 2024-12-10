from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:

    def __init__(self):
        self.car_handler = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        car = Turtle("square")
        car.up()
        car.goto(300, random.randint(-250, 250))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(COLORS[random.randint(0, 5)])
        self.car_handler.append(car)



    def move(self):
        for car in self.car_handler:
            car.backward(self.speed)


    def level_up(self):
        self.speed += MOVE_INCREMENT