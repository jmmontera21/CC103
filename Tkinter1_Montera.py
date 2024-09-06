from email.mime import image
from tkinter import *
from tkinter.ttk import Combobox
from turtle import bgcolor
screen=Tk()
screen.title('Welcome to Tkinter World')
screen.geometry("500x400+10+10")
screen.configure(bg='red')
lbl=Label(screen, text="This is simple Tkinter data", fg='green', bg='white', font=("Arial, 18"))
lbl.place(x=100, y=50)
var = StringVar()
var.set("10")
data=("10", "20", "30", "40", "50", "60", "70", "80", "90", "100")
cb=Combobox(screen,values=data)
cb.place(x=100, y=220)

lb=Listbox(screen, height=10, width=12, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=280, y=160)

x0=IntVar()
x0.set(1)
rb1=Radiobutton(screen, text="individual", variable=x0,value=1)
rb2=Radiobutton(screen, text="team", variable=x0,value=2)
rb1.place(x=160, y=90)
rb2.place(x=260, y=90)

x1 = IntVar()
x2 = IntVar()
Cb1 = Checkbutton(screen, text = "Basketball", variable = x1)
Cb2 = Checkbutton(screen, text = "Badminton", variable = x2)
Cb1.place(x=160, y=120)
Cb2.place(x=260, y=120)

screen.mainloop()