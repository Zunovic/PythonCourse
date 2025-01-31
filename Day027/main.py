import tkinter as tk


def calc_miles():
    # Kilometer werden ausgelesen, in Meilen umgewandelt und auf 2 Stellen nach dem Komma gerundet
    calc_result = float(km_input.get()) * 0.6214
    rounded_result = round(calc_result, 2)
    # Wichtig: Bei Veränderungen nur Methoden benutzen, da wir keinen scope haben (.config())
    calc_equals.config(text=rounded_result)


window = tk.Tk()
window.title("Kilometer zu Meilen-Rechner")
window.minsize(330,150)
window.config(padx=115, pady=30)

# Alle Widgets in Grid-Reihenfolge
empty_label1 = tk.Label()
empty_label1.grid(column=0, row=0)
empty_label1.config(padx=20)

km_input = tk.Entry(width=10)
km_input.grid(column=1, row=0)

kilometer = tk.Label(text="Km")
kilometer.grid(column=2, row=0)

equal_to = tk.Label(text="sind ≈")
equal_to.grid(column=0, row=1)

calc_equals = tk.Label(text="")
calc_equals.grid(column=1, row=1)

miles = tk.Label(text="Meilen")
miles.grid(column=2, row=1)

calc_button = tk.Button(text="Berechnen", command=calc_miles)
calc_button.grid(column=1, row=2)

window.mainloop()
