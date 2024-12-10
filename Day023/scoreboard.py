from tkinter.constants import BOTTOM
from turtle import Turtle

ALIGNMENT = "center"
CLICK_NOTIFY = "upper"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.up()
        self.goto(-200, 265)
        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)