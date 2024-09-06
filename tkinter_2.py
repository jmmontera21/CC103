from tkinter import *
fromt tkinter import ttk

root = Tk()
root.geometry("800x800")
root.title("Introduction to TKINTER")
root.configure(bg='lightblue')

#widgets
Label1 = ttk.Label(root, text="Username", font=('Arial, 20'), bg='lightblue')
Label1.pack

UsernameEntry= ttk.Entry(root, width=50)
UsernameEntry.pack

Label2= Label(root, text="Password", font=('Arial, 20'), bg='lightblue')
Label2.pack

