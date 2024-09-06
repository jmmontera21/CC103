from tkinter import *


root=Tk()
root.geometry('940x600')
filename=PhotoImage(file="C:\\Users\\RLF\\Desktop\\CC103 Mesiera\\john-1.jpg")
background_ =Label(root,image=filename)
background_.place(x=0,y=0,relwidth=1,relheight=1)
root.title('Microsoft Office : Created By John Eric A. Cea')

FirstLabel1 = Label(root, text='Welcome to Microsoft Office' , font=('Arial',16 ), bg='White' , fg='black')
FirstLabel1.pack()
 
Button1 = Button(root, text='Click here to launch Word Microsoft' , font=('Times Roman',10 ), bg='cyan' , fg='black' , command=click)
Button1.pack()


FirstLabel2 = Label(root, text='Welcome to Powerpoint' , font=('Arial',16 ), bg='White' , fg='black')
FirstLabel2.pack()

Button2 = Button(root, text='Click here to launch Powerpoint' , font=('Times Roman',10 ), bg='Red' , fg='black' , command=click_2)
Button2.pack()

FirstLabel3 = Label(root, text='Welcome to Excel' , font=('Arial',16 ), bg='White' , fg='black')
FirstLabel3.pack()

Button3 = Button(root, text='Click here to launch Excel' , font=('Times Roman',10 ), bg='Green' , fg='black' , command=click_3)
Button3.pack()


root.mainloop()