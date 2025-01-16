import turtle
import pandas


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = 0

game_state = True

while game_state:
    user_answer = screen.textinput(f"Errate den US Staat {correct_answers}/50", "Wie heißen die anderen Staaten?").title()
    if user_answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.up()
        state_data = data[data.state == user_answer]
        # .item() die richtigen Values weitergegeben werden.
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)
        all_states.remove(user_answer)
        correct_answers += 1




screen.exitonclick()