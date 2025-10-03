from tkinter import  *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letter_choice = range(0, 26)
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 3)
nr_numbers = random.randint(2,4)
def set_password():
    password_list = []

    for character in range(0, nr_letters):
        password_list.append(random.choice(letters))
    for character in range(0, nr_symbols):
        password_list.append(random.choice(symbols))
    for character in range(0, nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)

    shuffled_password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(END, f"{shuffled_password}")

#OR YOU CAN USE A FOR LOOP TO TURN THE LIST BACK INTO A STRING:
# password = ""
# for character in password_list:
#       password += character
# print(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    saved_web = website_input.get()
    saved_email = email_input.get()
    s_password = password_input.get()

    if saved_email == "" or s_password == "" or saved_web == "":
        messagebox.showinfo(title="Oops!", message="You left a field empty!")
    else:
        go_ahead = messagebox.askokcancel(title="Save Password info.", message=f"Website: {saved_web}\n"
                                                                           f" Email: {saved_email}\n Password: {s_password}\n"
                                                                           f" Do you want to go ahead?")
        if go_ahead:
            with open("saved_password.txt", mode="a") as password_file:
                password_file.write(f"{saved_web} |{saved_email} | {s_password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Palazzo's Password Manager.")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 111, image=logo_img)
# canva_text = canvas.create_text(103, 130, fill="white", text="00:00", font=(FONT_NAME, 45, "bold"))
canvas.grid(column=1, row=0)

#labels
website = Label(text="Website:")
email = Label(text= "Email/Username:")
password = Label(text= "Password:")

website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)


#Inputs
website_input = Entry(width=50)
website_input.focus()
email_input = Entry(width=50)
email_input.insert(END, "palazzo@gmail.com")

password_input = Entry(width=30)

website_input.grid(column=1,columnspan=3, row=1)
email_input.grid(column=1,columnspan=3,row=2)
password_input.grid(column=1,  row=3)


#Buttons
gen_password = Button(text="Generate Password", command=set_password)
add_password = Button(text="Add", width=40, command=save_password)

gen_password.grid(column=2,  row=3)
add_password.grid(column=1, columnspan=2, row=4)








window.mainloop()