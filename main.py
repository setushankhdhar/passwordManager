from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email} "
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("🔐 Password Manager")
window.config(padx=50, pady=50, bg="#f0f4f7")

# Canvas (Logo)
canvas = Canvas(height=200, width=200, bg="#f0f4f7", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
label_font = ("Arial", 12, "bold")

website_label = Label(text="Website:", font=label_font, bg="#f0f4f7")
website_label.grid(row=1, column=0, sticky="e", pady=5)

email_label = Label(text="Email/Username:", font=label_font, bg="#f0f4f7")
email_label.grid(row=2, column=0, sticky="e", pady=5)

password_label = Label(text="Password:", font=label_font, bg="#f0f4f7")
password_label.grid(row=3, column=0, sticky="e", pady=5)

# Entry fields
entry_font = ("Arial", 11)

website_entry = Entry(width=33, font=entry_font, bd=2, relief=GROOVE)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=33, font=entry_font, bd=2, relief=GROOVE)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "setushankhdhar95@gmail.com")

password_entry = Entry(width=21, font=entry_font, bd=2, relief=GROOVE)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, bg="#4CAF50", fg="white",
                                  font=("Arial", 10, "bold"), padx=5, pady=2, activebackground="#45a049")
generate_password_button.grid(row=3, column=2, padx=5)

add_button = Button(text="Add", width=36, command=save, bg="#2196F3", fg="white",
                    font=("Arial", 10, "bold"), pady=5, activebackground="#1e88e5")
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
