from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def set_cords(self, direction):
        if direction:
            self.goto(350, 0)
        else:
            self.goto(-350, 0)




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(0, 265)
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
