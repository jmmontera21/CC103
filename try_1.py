x = int(input("Please enter a number: "))
option = input("What do you want to do with this number?""(square, cube, factorial)")
if option == ("square"):
    def square(a):
        if a == 1:
            return a
        else:
            return x*x
print("square of ",x, " : ",end="")
print(square(x))

if option == ("cube"):
    def cube(b):
        if b == 1:
            return b
        else:
            return x*x*x
print("square of ",x, " : ",end="")
print(cube(x))

if option == ("factorial"):
    def factorial(c):
        if c == 1:
            return c
        else:
            return c*factorial(c-1)
print("factorial of ",x," : ",end="")
print(factorial(x))