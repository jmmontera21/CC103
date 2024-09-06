from ast import operator
from math import factorial
from mimetypes import common_types
from multiprocessing.connection import answer_challenge
from statistics import variance
from tkinter import * 
import math

root = Tk()
root.title("Simple Calculator")
root.geometry("460x420")
root.configure(bg='lightgreen')

num_input = Entry(root, width=27,font=('Arial',22), borderwidth=5, justify=RIGHT)
num_input.place(x=8, y=10)
    
def display_number(x_number):
    current_input = num_input.get()
    num_input.delete(0, END)
    num_input.insert(0, current_input + x_number)

def delete_number():
    num_input.delete(0, END)

def selected_operator(opr):
    global firstnum
    global operator
    firstnum = eval(num_input.get())
    print(firstnum)
    num_input.delete(0,END)
    operator = opr
    print(operator)

def square_root():
    global firstnum
    global operator
    firstnum = eval(num_input.get())
    num_input.delete(0,END)
    num_input.insert(0, (math.sqrt(firstnum)))

def factorial_number():
    global firstnum
    global operator
    firstnum = eval(num_input.get())
    num_input.delete(0,END)
    num_input.insert(0,(math.factorial(firstnum)))

def square_number():
    global firstnum
    global operator
    firstnum = eval(num_input.get())
    num_input.delete(0,END)
    answer = firstnum * firstnum 
    num_input.insert(0, answer)

def cube_number():
    global firstnum
    global operator
    firstnum = eval(num_input.get())
    num_input.delete(0,END)
    answer = firstnum * firstnum * firstnum
    num_input.insert(0, answer)

def equals_computation():
    global secondnum
    global answer
    secondnum = eval(num_input.get())
    num_input.delete(0,END)

    if operator == '+':
        answer = firstnum + secondnum
        num_input.insert(0, answer)
    elif operator == '-':
        answer = firstnum - secondnum
        num_input.insert(0, answer)
    elif operator == '*':
        answer = firstnum * secondnum
        num_input.insert(0, answer)
    elif operator == '/':
        answer = firstnum / secondnum
        num_input.insert(0, answer)
    elif operator == 'x^y':
        answer = firstnum ** secondnum
        num_input.insert(0, answer)
    else:
        print("Error")


num1 = Button(root, text="1", height=1, width=4, font=('Helvetica', 20), borderwidth=4,command=lambda:display_number("1"))
num2 = Button(root, text="2", height=1, width=4, font=('Helvetica', 20), borderwidth=4,command=lambda:display_number("2"))
num3 = Button(root, text="3", height=1, width=4, font=('Helvetica', 20), borderwidth=4,command=lambda:display_number("3"))
num4 = Button(root, text="4", height=1, width=4, font=('Helvetica', 20), borderwidth=4,command=lambda:display_number("4"))
num5 = Button(root, text="5", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("5"))
num6 = Button(root, text="6", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("6"))
num7 = Button(root, text="7", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("7"))
num8 = Button(root, text="8", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("8"))
num9 = Button(root, text="9", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("9"))
num0 = Button(root, text="0", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("0"))
dot = Button(root, text=".", height=1, width=4, font=('Helvetica', 20),borderwidth=4,command=lambda:display_number("."))

delete = Button(root, text="del", height=1, width=4, font=('Helvetica', 20), borderwidth=4, command=lambda:delete_number())

plus = Button(root, text ="+", height=1, width=4, font=('Helvetica',20), bg='lightblue', borderwidth=4,command=lambda:selected_operator("+"))
minus = Button(root, text="-", height=1, width=4, font=('Helvetica', 20), bg='lightblue', borderwidth=4, command=lambda:selected_operator("-"))
times = Button(root, text="X", height=1, width=4, font=('Helvetica', 20), bg='lightblue', borderwidth=4, command=lambda:selected_operator("*"))
divide = Button(root, text="/", height=1, width=4, font=('Helvetica', 20), bg='lightblue', borderwidth=4, command=lambda:selected_operator("/"))
x_power_y = Button(root, text="x^y", height=1, width=12, font=('Helvetica', 20), bg='yellow', borderwidth=4, command=lambda:selected_operator("x^y"))
cube = Button(root, text="x³", height=1, width=4, font=('Helvetica', 20), bg='pink', borderwidth=4, command=lambda:cube_number())
factorial = Button(root, text="x!", height=1, width=4, font=('Helvetica', 20), bg='pink', borderwidth=4, command=lambda:factorial_number())
root_square = Button(root, text="√", height=1, width=4, font=('Helvetica', 20), bg='pink', borderwidth=4, command=lambda:square_root())
square = Button(root, text="x²", height=1, width=4, font=('Helvetica', 20), bg='pink', borderwidth=4, command=lambda:square_number())
equals = Button(root, text="=", height=1, width=12, font=('Helvetica', 20), bg='orange', borderwidth=4, command=lambda:equals_computation())
#grids

#ROW1
num1.place(x=10, y=70)
num2.place(x=100, y=70)
num3.place(x=190, y=70)



#ROW2
num4.place(x=10, y=140)
num5.place(x=100, y=140)
num6.place(x=190, y=140)

#ROW3
num7.place(x=10, y=210)
num8.place(x=100, y=210)
num9.place(x=190, y=210)

#ROW4
num0.place(x=100, y=280)
dot.place(x=190, y=280)
delete.place(x=10, y=280)

#COLUMN 4
plus.place(x=280, y=70)
minus.place(x=280, y=140)
times.place(x=280, y=210)
divide.place(x=280, y=280) 
square.place(x=370, y=70)
cube.place(x=370, y=140)
factorial.place(x=370, y=210)
root_square.place(x=370, y=280)
x_power_y.place(x=10,y=350 )
equals.place(x=240, y=350)

root.mainloop()