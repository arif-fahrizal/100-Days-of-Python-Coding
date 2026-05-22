from tkinter import *

window = Tk()
window.title("First GUI Program With Tkinter")
window.minsize(500, 300)

# Label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)

label["text"] = "New Text"
label.config(text="New Text")

# Button
def button_clicked():
    # label["text"] = "Button Got Clicked"
    label["text"] = input.get()

button1 = Button(text="Click Me", command=button_clicked)
button1.grid(row=1, column=1)

button2 = Button(text="Other Click Me", command=button_clicked)
button2.grid(row=0, column=2)

# Entry / Textbox / Input
input = Entry(width=10)
input.grid(row=2, column=3)



window.mainloop()