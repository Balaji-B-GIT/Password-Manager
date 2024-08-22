# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row = 0,column = 1)

# labels--------------------------------------------------------------------------------------------------------------
website_text = Label(text="Website:")
website_text.grid(row = 1,column = 0)

email_text = Label(text="Email/Username:")
email_text.grid(row = 2,column = 0)

pass_text = Label(text="Password:")
pass_text.grid(row = 3,column = 0)

# entries--------------------------------------------------------------------------------------------------------------
website_input = Entry(width=35)
website_input.grid(row = 1,column = 1, columnspan=2, sticky = EW)
# the "sticky" parameter, the EW part is the compass directions (E)ast and (W)est and the sticky basically "sticks" the
# widget to the edges of the column.

email_input = Entry(width=35)
email_input.grid(row = 2,column = 1, columnspan=2, sticky = EW)

pass_input = Entry(width=21)
pass_input.grid(row = 3,column = 1, sticky = EW)

# buttons------------------------------------------------------------------------------------------------------------
generate_pass = Button(text = "Generate Password")
generate_pass.grid(row = 3,column = 2, sticky = EW)

add_pass = Button(text = "Add",width=36)
add_pass.grid(row = 4,column = 1, columnspan=2, sticky = EW)






window.mainloop()
