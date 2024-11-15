import turtle as t

draw = t.Turtle()
screen = t.Screen()


def move_forward():
    draw.forward(10)


def move_backward():
    draw.backward(10)


def turn_left():
    new_heading = draw.heading() + 10
    draw.setheading(new_heading)


def turn_right():
    new_heading = draw.heading() - 10
    draw.setheading(new_heading)


def clear_screen():
    draw.up()
    draw.clear()
    draw.setposition(0, 0)
    draw.down()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()
