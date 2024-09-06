
from tkinter import *
#root meaning the main window
root = Tk()
#geometry function is used for setting up the size of the root window
root.geometry('1000x800')
root.title('This is my first UI')

FirstLabel1 = Label(root, text='Welcome to my first UI', font=('Arial,16'), bg='lightgray', fg='black')
FirstLabel1.pack()

Button = Button(root, text='Click Here to Play', font=('Arial,10'), bg='lightgray', fg='black')
Button.pack()

root.mainloop()