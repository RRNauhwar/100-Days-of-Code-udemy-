from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
password_list = password_letters + password_symbols + password_numbers
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")
def generate_password():
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("data.txt","a")as data_file:
        data_file.write(f"{website_entry.get()}|{email_entry.get()}|{password_entry.get()}\n")
        website_entry.delete(0,END) # to clear the website entry field because after adding the data it should be empty
        password_entry.delete(0,END) # to clear the password entry field because after adding the data it should be empty
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")

# title_label = Label(text="Password Manager",font=("Arial",24,"bold"),bg="white",fg="black")
# title_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=1,column=1)

website_label = Label(text="Website:",bg="white",fg="black")
website_label.grid(row=2,column=0)
website_entry = Entry(width=35)
website_entry.grid(row=2,column=1,columnspan=2)
website_entry.focus()
email_label = Label(text="Email/Username:",bg="white",fg="black")
email_label.grid(row=3,column=0)
email_entry = Entry(width=35)
email_entry.grid(row=3,column=1,columnspan=2)
email_entry.insert(0,"Enter email")
password_label = Label(text="Password:",bg="white",fg="black")
password_label.grid(row=4,column=0)
password_entry = Entry(width=21)
password_entry.grid(row=4,column=1)
generate_password = Button(text="Generate Password",bg="white",fg="black",width=14,command=generate_password)
generate_password.grid(row=4,column=2)
add_button = Button(text="Add",bg="white",fg="black",width=36,command=save_password)
add_button.grid(row=5,column=1,columnspan=2)



window.mainloop()