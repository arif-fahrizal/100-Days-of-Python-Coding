from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_input.insert(0, generated_password)
    # pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_save = website_input.get()
    email_save = email_input.get()
    password_save = password_input.get()
    new_data = {
        website_save: {
            "email": email_save,
            "password": password_save
        }
    }

    if len(website_save) == 0 or len(email_save) == 0:
        messagebox.askokcancel(title="Oops", message=f"Please make sure you haven't left any fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)                 # Load dan Read data
        except FileNotFoundError:
            data = {}

        data.update(new_data)                               # Updating old data
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)            # Save data JSON


        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data File Not Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=150, height=150)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)

# Label
website = Label(text="Website:")
email = Label(text="Email/Username:")
password = Label(text="Password:")

# Input
website_input = Entry(width=35)
website_input.focus()
email_input = Entry(width=55)
email_input.insert(0, "example@gmail.com")
password_input = Entry(width=35)

# Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
add_button = Button(text="Add", width=45, command=save)
search_button =Button(text="Search", width=14, command=find_password)

# Positions
canvas.grid(row=0, column=1)
website.grid(row=1, column=0, sticky="e", padx=5, pady=5)
email.grid(row=2, column=0, sticky="e", padx=5, pady=5)
password.grid(row=3, column=0, sticky="e", padx=5, pady=5)

website_input.grid(row=1, column=1, sticky="w", padx=5, pady=5)
email_input.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)
password_input.grid(row=3, column=1, sticky="w", padx=5, pady=5)

generate_button.grid(row=3, column=2, padx=5, pady=5)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
search_button.grid(row=1, column=2)



window.mainloop()
