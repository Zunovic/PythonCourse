from tkinter import *

# Beispiel eines Windows
window = Tk()
window.title("Tkinter Widgets")
window.minsize(width=500, height=500)

#Labels
label = Label(text="Text")
label.config(text="New Text")
label.pack()

# Buttons
def action():
    print("Button click")

# Buttons die funktionen aufrufen
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
entry.insert(END, string="Text Beispiel")
# get nimmt den Text aus dem Entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Cursor innerhalb der Textbox
text.focus()
text.insert(END, "Multiline Beispiel-Text zum Veranschaulichen")
# get nimmt den Buchstaben an pos 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    # get nimmt die value innerhalb der Spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
# Slider von 0 bis 100 der die Value ausgibt
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # Gibt 1 aus, wenn an und 0 wenn aus
    print(checked_state.get())
# IntVar speichert den aktuellen Integer (0 oder 1)
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
# Selbes wie bei Checkbutton nur dass 1 oder 2 gespeichert wird
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # get gibt die aktuelle Auswahl zurück
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"] # Einträge können beliebig lang sein
# müssen aber in Listbox(height) angepasst werden. (Scrollen geht aber auch)
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

