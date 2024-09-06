x = int(input("Please enter a number: "))
def square(a):
    if a == 1:
        return a
    else:
        return x*x*x
print("square of ",x, " : ",end="")
print(square(x))