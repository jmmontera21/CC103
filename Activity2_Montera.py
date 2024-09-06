from tkinter import *
from tkinter.tix import ButtonBox
  
root = Tk()
root.title('Find & Replace')
root.geometry('670x160')
root.grid

entry1 = Entry(root, width=80)
entry1.place(x=80, y=15)

entry2 = Entry(root, width=80)
entry2.place(x=80, y=45)

FirstLabel1 = Label(text='Find:',font=('Calibri',11), fg='blue')
FirstLabel1.place(x=38, y=12)

FirstLabel2 = Label(text='Replace:',font=('Calibri',11), fg='blue')
FirstLabel2.place(x=15, y=42)

FirstLabel3 = Label(text='Direction:',font=('Calibri',11), fg='black')
FirstLabel3.place(x=300, y=72)

Checkbutton1 = Checkbutton(text='Match Whole Word Only', font=('Calibri',11), fg='black')
Checkbutton1.place(x=85, y=70)

Checkbutton2 = Checkbutton(text='Match Case', font=('Calibri',11), fg='black')
Checkbutton2.place(x=85, y=100)

Checkbutton3 = Checkbutton(text='Wrap Around', font=('Calibri',11), fg='black')
Checkbutton3.place(x=85, y=130)

var=IntVar()
Radiobutton1 = Radiobutton(text='Up', font=('Calibri',11), fg='black', variable=var, value=1)
Radiobutton1.place(x=310, y=100)

Radiobutton2 = Radiobutton(text='Down', font=('Calibri',11), fg='black', variable=var, value=2)
Radiobutton2.place(x=460, y=100)

Button1 = Button(text='Find', font=('Calibri',11), fg='black', bg='lightblue')
Button1.place(x=580, y=10, width=85)

Button2 = Button(text='Find all', font=('Calibri',11), fg='black', bg='pink')
Button2.place(x=580, y=45, width=85)

Button3 = Button(text='Replace', font=('Calibri',11), fg='black', bg='lightgreen')
Button3.place(x=580, y=80, width=85)

Button4 = Button(text='Replace All', font=('Calibri',11), fg='black', bg='yellow')
Button4.place(x=580, y=115, width=85)
root.mainloop()
