#Develop a python file that will ask a user a number, then the program will ask the user what he/she wants to do with the number, the first option is to get the square of the number second is to to get the cube of the number and last option is to get the factorial of a number. The program would require three functions that responds to those three(3) options and all three must have a return statement. 

print("\t\t ~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\t Square, Cube, Factorial")
print("\t\t ~~~~~~~~~~~~~~~~~~~~~~~")
print("\t")

a = 0
def square():
    a = int(input("Please input the number you want to get the square of: "))
    if a == 1:
        return a
    else:
        square = a*a
        return square

def cube():
    a = int(input("Please input the number you want to get the cube of: "))
    if a == 1:
        return a
    else:
        cube = a*a*a
        return cube

def factorial():
    a = int(input("Please input the number you want to get the factorial of: "))
    factorial = 1
    if a == 1:
        return a
    else:
        for x in range(1,a + 1):
            factorial = factorial*x
        return factorial

print("\nType 'square' if you want to get the square of the number. \nType 'cube' if you want to get the cube of the number. \nType 'factorial' if you want to get the factorial of the number.")
operations = input("Enter the option you want: ")
if operations == 'square':
    print(square()), print("is the square of that number.")
elif operations == 'cube':
    print(cube()), print("is the cube of that number.")
elif operations == 'factorial':
    print(factorial()), print("is the factorial of that number.")
else:
    print("Invalid operation.")

