import tkinter as tk

window = tk.Tk()
window.title("First GUI")
window.minsize(400, 300)

label_1 = tk.Label(text="hi", font=("Arial", 24, "bold"))
label_1.pack(side="right")

window.mainloop()