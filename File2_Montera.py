#Create a python function that will accept 7 numbers with decimal values and wont accept value if it isn't a float value. After accepting the values, determine the number with the highest values among the given, and then return that value for printing. 
print("\t\t ~~~~~~~~~~~~~")
print("\t\t Decimal Value")
print("\t\t ~~~~~~~~~~~~~")
print("\t")

no = []
def decimal():
    return
for a in range(7):
    number = float(input("Enter number for index " + str(a) + " : "))
    no.append(number)
    if number in range (1,99999):
        print("Invalid input")
        break
    else:
        continue

print("List :", no)
print("The highest value in the list is", max(no))







