from tkinter import *
import random
from tkinter import messagebox
import json
import pyperclip

FONT = ("Arial", 10, "normal")


def find_password():
    """
    It opens the data file, loads the data, checks if the website exists in the data, and if it does, it
    displays the email and password for the website
    """
    try:
        with open("password_data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")
    else:
        website = website_entry.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=f"{website}", message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showerror("Error", "No details for the website exists")


def password_gen():
    """
    It creates a list of letters, numbers, and symbols, then adds a random selection of each to a new
    list, shuffles the list, and joins the list into a string
    """
    password_entry.delete(0, END)

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(1, 7))
    password_list.extend(random.choice(symbols) for _ in range(1, 5))
    password_list.extend(random.choice(numbers) for _ in range(1, 7))

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


def save_password():
    """
    If the user has entered all the required information, then the function will save the data to a JSON
    file
    """
    website = website_entry.get()
    user = email_entry.get()
    password = password_entry.get()

    new_data = {website: {"email": user, "password": password}}

    if len(website) == 0 and len(user) == 0 and len(password) == 0:
        messagebox.showerror("Error", "Please fill all entries")
    else:
        try:
            with open("password_data.json") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("password_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.config(font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.config(width=33)
website_entry.grid(row=1, column=1)

search_btn = Button(text="Search", command=find_password)
search_btn.config(width=14)
search_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.config(font=FONT)
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.insert(END, "example@gmail.com")
email_entry.config(width=52)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.config(font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.config(width=33)
password_entry.grid(row=3, column=1)

generate_pwd = Button(text="Generate Password", command=password_gen)
generate_pwd.config(width=14)
generate_pwd.grid(row=3, column=2)

add_btn = Button(text="Add", command=save_password)
add_btn.config(width=44)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()

# https://tkdocs.com/tutorial/widgets.html#entry
