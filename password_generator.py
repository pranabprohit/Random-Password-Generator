from tkinter import *
import random
import pyperclip, string

root = Tk()
root.geometry("350x350")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate_password():
    alpha= str(string.ascii_letters)
    symbol= str(string.punctuation)
    numbers= str(string.digits)

    char = alpha + symbol + numbers
    password = "".join(random.choice(char) for i in range(passlen.get()))
    passstr.set(password)

def copy():
    random_password = passstr.get()
    pyperclip.copy(random_password)        


root.title("Random Password Generator")
lbl = Label(root,text = 'Generate a random password.', font = ("Arial bold",15))
lbl.place(x=34,y=10)

lbl1 = Label(root,text = 'Length :', font = ("Arial bold",11))
lbl1.place(x=52,y=90)

ent = Entry(root, textvariable=passlen)
ent.place(x=120,y=90)

lbl2 = Label(root,text = 'Password :', font = ("Arial bold",11))
lbl2.place(x=34,y=130)

pwd = Entry(root, textvariable=passstr)
pwd.place(x=120,y=130)

btn1 = Button(root,text = 'Generate Password', bg = 'grey', fg ='white', command = generate_password)
btn1.place(x=85,y=180)

btn2 = Button(root,text = 'Copy', bg = 'grey', fg = 'white', command = copy)
btn2.place(x=225,y=180) 
root.mainloop()