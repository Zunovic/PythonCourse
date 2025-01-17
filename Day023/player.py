from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("red")
        self.setheading(90)


    def move_fd(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)