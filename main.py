from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    input_password_var.delete(0, END)
    input_password_var.insert(index=0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = input_web_var.get()
    email = input_email_var.get()
    password = input_password_var.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message=f"Please Dont leave any filed empty")
    else:
        try:
            with open("data.json", 'r') as file1:
                # file1.write(f"{website} | {email} | {password} \n")
                # json.dump(new_data, file1, indent=4)
                data = json.load(file1)
        except FileNotFoundError:
            with open("data.json", "w") as file1:
                json.dump(new_data, file1, indent=4)
        else:
            data.update(new_data)

            with open("data.json", 'w') as file1:
                # file1.write(f"{website} | {email} | {password} \n")
                json.dump(data, file1, indent=4)
        finally:
            input_email_var.delete(0, END)
            input_web_var.delete(0, END)
            input_password_var.delete(0, END)

            input_email_var.insert(index=0, string="@email.com")

            input_web_var.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = input_web_var.get()
    try:
        with open("data.json", 'r') as file1:
            data = json.load(file1)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data exist")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website,
                                message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",
                                message=f"No saved data for this {website}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=E)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2, sticky=E)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=E)

input_web_var = Entry(width=32)
input_web_var.grid(column=1, row=1)
input_web_var.focus()

input_email_var = Entry(width=32)
input_email_var.grid(column=1, row=2)
input_email_var.insert(index=0, string="@email.com")

input_password_var = Entry(width=32, show="*")
input_password_var.grid(column=1, row=3)

search_button = Button(text="Search", width=16, bg='sky blue',
                       command=search_password, )
search_button.grid(column=2, row=1)

gen_pass_button = Button(text="Generate Password", width=16,
                         bg='coral1', command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, bg='pale green', command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
