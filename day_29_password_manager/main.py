from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend([random.choice(letters) for _ in range(nr_letters)])

    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])

    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_entry.get():
            {
                "email":email_entry.get(),
                "password":password_entry.get()
            }
    }
    if len(email_entry.get()) == 0 or \
            len(password_entry.get()) == 0 or \
            len(website_entry.get()) == 0:
        messagebox.showerror(title="Missing fields value", message="You've left some fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered: \nEmail: {email_entry.get()}\nPassword: {password_entry.get()} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file_to_write:
                    old_data = json.load(file_to_write)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                old_data.update(new_data)
                with open("data.json", "w") as file_to_write:
                    json.dump(old_data, file_to_write, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if data.get(website_entry.get()):
                messagebox.showinfo(title=website_entry.get(),
                                       message=f"These are the informations: \nEmail: {data[website_entry.get()]['email']}\nPassword: {data[website_entry.get()]['password']} \n.")
            else:
                messagebox.showinfo(title="Error",
                                    message=f"No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message=f"No data file found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(
    100,
    100,
    image=tomato_img
)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "teste@gmail.com")
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_generation_button = Button(text="Generate Password", command=generate_password)
password_generation_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
