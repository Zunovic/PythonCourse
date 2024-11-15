import turtle as t
import random
import colorgram
rgb_color = []
colors = colorgram.extract('proxy-image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

screen = t.Screen()
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.setheading(225)
tim.up()
tim.forward(400)
tim.setheading(90)
for _ in range(5):
    for _ in range(2):
        for _ in range(10):
            tim.down()
            tim.dot(20, random.choice(rgb_color))
            tim.up()
            tim.fd(50)
        tim.right(90)
        tim.fd(50)
        tim.right(90)
        tim.fd(50)
    tim.right(90)
    tim.fd(100)
    tim.left(90)

screen.exitonclick()
