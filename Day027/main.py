import tkinter as tk


def button_clicked():
    print("Button clicked")
    new_label = my_input.get()
    label_1.config(text=new_label)

window = tk.Tk()
window.title("First GUI")
window.minsize(400, 300)

# Label
label_1 = tk.Label(text="Type something", font=("Arial", 24))
label_1.pack()

# Button
button = tk.Button(text="Click", command=button_clicked)
button.pack()

# Inputs
my_input = tk.Entry()
my_input.pack()

window.mainloop()
