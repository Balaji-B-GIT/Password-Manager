from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generated_password():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [choice(letters) for i in range(randint(8, 10))]
    rand_numbers = [choice(numbers) for j in range(randint(2, 4))]
    rand_symbols = [choice(symbols) for k in range(randint(2, 4))]
    password = rand_letters + rand_numbers + rand_symbols
    shuffle(password)
    shuffled_password = "".join(password)

    pass_input.insert(index=0, string=shuffled_password)
    # copies password to clipboard
    pyperclip.copy(shuffled_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    user_data = {
        website : {
            "email": email,
            "password": password
            }
        }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Are you blind?", message= "Some of the fields are empty!!!")
    else:
        try:
            with open("password_db.json",mode="r") as file:
                data = json.load(file)
                data.update(user_data)
            with open("password_db.json", "w") as file:
                json.dump(data, file, indent=4)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
            with open("password_db.json", "w") as file:
                json.dump(user_data, file, indent=4)
        finally:
            website_input.delete(0,"end")
            email_input.delete(0,"end")
            pass_input.delete(0, "end")
            website_input.focus()
            messagebox.showinfo(title="",message="Saved Successfully")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("password_db.json", mode="r") as file:
            data = json.load(file)
        if website in data:
            messagebox.showinfo(title=website, message=f"Email : {data[website]["email"]}\n"
                                                       f"Password : "f"{data[website]["password"]}")
        elif len(website) == 0:
             messagebox.showinfo(title="Are you blind?", message="Text Field Is Empty")
        else:
            messagebox.showinfo(title="Error", message=f"No Details Of The {website} Exists")

        # for i in data:
        #     if website == i:
        #         messagebox.showinfo(title=website,message=f"Email : {data[i]["email"]}\nPassword : "
        #                                                     f"{data[i]["password"]}")
        #     elif len(website) == 0:
        #         messagebox.showinfo(title="Are you blind?", message="Text Field Is Empty")
        #         break
        #     elif website not in data:
        #         messagebox.showinfo(title="Error", message="No Details Of The Website Exists")
        #         break

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row = 0,column = 1)

# LABELS--------------------------------------------------------------------------------------------------------------
website_text = Label(text="Website:",padx=5,pady=5)
website_text.grid(row = 1,column = 0)

email_text = Label(text="Email/Username:",padx=5,pady=5)
email_text.grid(row = 2,column = 0)

pass_text = Label(text="Password:",padx=5,pady=5)
pass_text.grid(row = 3,column = 0)

# ENTRIES--------------------------------------------------------------------------------------------------------------
website_input = Entry(width=32)
website_input.grid(row = 1,column = 1, sticky = W)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row = 2,column = 1, columnspan=2, sticky = EW)

pass_input = Entry(width=32)
pass_input.grid(row = 3,column = 1, sticky = W)

# BUTTONS------------------------------------------------------------------------------------------------------------
search_pass = Button(text = "Search", command=find_password)
search_pass.grid(row = 1,column = 2, sticky = EW)
# the "sticky" parameter, the EW part is the compass directions (E)ast and (W)est and the sticky basically "sticks" the
# widget to the edges of the column.

generate_pass = Button(text = "Generate Password", command=generated_password)
generate_pass.grid(row = 3,column = 2, sticky = EW)

add_pass = Button(text = "Add",width=36, command=save)
add_pass.grid(row = 4,column = 1, columnspan=2, sticky = EW,pady=5)


window.mainloop()