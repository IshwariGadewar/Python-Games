import tkinter
import tkinter.messagebox
import random
import pyperclip # type: ignore
import json

PATH = r'D:\PYTHON\PYTHON - Udemy\Game\Password Manager\logo.png'
PATH_DATA = r'D:\PYTHON\PYTHON - Udemy\Game\Password Manager\data.json'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nl = random.randint(8,10)
    nn = random.randint(2,4)
    ns = random.randint(2,4)

    pass_rand = []
    for char in range(nl):
        pass_rand.append(random.choice(letters))
    for char in range(nn):
        pass_rand.append(random.choice(numbers))
    for char in range(ns):
        pass_rand.append(random.choice(symbols))

    random.shuffle(pass_rand)
    password = "".join(pass_rand)

    pass_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SEARCH ------------------------------- #

def search():
    website = web_entry.get()
    try:
        with open(PATH_DATA,'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title=f"{website}",message=f"Email: {email}\nPassword: {password}")
        else:
            tkinter.messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website)==0 or len(password)==0:
        tkinter.messagebox.showinfo(title="Oops",message="Please make sure you haven't left anything empty")
    else:
        try:
            with open(PATH_DATA,'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(PATH_DATA,'w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:    
            data.update(new_data)
            with open(PATH_DATA,'w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0,tkinter.END)
            pass_entry.delete(0,tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

#creating window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#logo
canvas = tkinter.Canvas(width=200,height=200)
logo = tkinter.PhotoImage(file=PATH)
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

#website details
web_text = tkinter.Label(text="Website:")
web_text.grid(row=1,column=0)
web_entry = tkinter.Entry(width=35)
web_entry.grid(row=1,column=1)
web_entry.focus()
web_search = tkinter.Button(text="Search",width=15,bg="blue",command=search)
web_search.grid(row=1,column=2)

#email details
email_text = tkinter.Label(text="Email/Username:")
email_text.grid(row=2,column=0)
email_entry = tkinter.Entry(width=45)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"gadewareshwari24@gmail.com")

#password
pass_text = tkinter.Label(text="Password:")
pass_text.grid(row=3,column=0)
pass_entry = tkinter.Entry(width=35)
pass_entry.grid(row=3,column=1)
Gen_pass = tkinter.Button(text="Generate Password",command=gen_pass,width=15)
Gen_pass.grid(row=3,column=2)

#add
add = tkinter.Button(text="Add",width=46,command=save)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()