from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    count_down(0)
    canvas.itemconfig(timer_text, text="05:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute_count = math.floor(count / 60)
    seconds_count = count % 60
    canvas.itemconfig(timer_text, text=f"{minute_count}:{seconds_count}")
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro-Lernen")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


timer = Label()
timer.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label()
check_marks.config(fg=GREEN, bg=YELLOW, text="✔", font=(FONT_NAME, 10))
check_marks.grid(column=1, row=3)

window.mainloop()
