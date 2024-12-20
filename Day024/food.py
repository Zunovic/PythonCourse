from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self. shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.new_spot()

    def new_spot(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)