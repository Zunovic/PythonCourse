import turtle
import pandas

# Test für alle Staaten
def test_quiz():
    for i in all_states:
        tt = turtle.Turtle()
        tt.hideturtle()
        tt.up()
        t_state_data = data[data.state == i]
        tt.goto(t_state_data.x.item(), t_state_data.y.item())
        tt.write(i)


data = pandas.read_csv("50_states.csv")
#Alle Staaten werden in eine Liste gespeichert
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("US States Game")
# Image muss ein gif sein, weil es das einzige Dateiformat ist, was Turtle unterstützt
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = 0

# test_quiz()
# ^- Für den Test die ganze While Schleife auskommentieren
while all_states:
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

#while all_states:
    #user_answer = screen.textinput(f"Errate den US Staat {correct_answers}/50", "Wie heißen die anderen Staaten?").title()







screen.exitonclick()