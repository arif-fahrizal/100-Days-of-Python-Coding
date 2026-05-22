from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


def convert():
    km_result["text"] = float(miles_input.get()) * 1.609

# Label
miles = Label(text="Miles")
km = Label(text="Km")
km_result = Label(text="0")
equal_to = Label(text=":")

# Textbox
miles_input = Entry(width=9)

# Button
btn = Button(text="Calculate", command=convert)

# Position
miles.grid(row=0, column=2)
km.grid(row=1, column=2)
km_result.grid(row=1, column=1)
equal_to.grid(row=1, column=0)
miles_input.grid(row=0,column=1)
btn.grid(row=2, column=1)




window.mainloop()