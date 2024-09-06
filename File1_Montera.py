#Create a function that will accept a person's name and age, address, birthdate, email, if he/she has a job, what is the job title, and put all those data in a dictionary. 

print("\t\t ****************")
print("\t\t Personal Details")
print("\t\t ****************")
print("\t")

personal_details = {}
def biodata():
    return 
while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    birthday = input("Enter your birthdate: ")
    email = input("Enter your email address: ")
    job = input("Do you have a job?""(yes/no)")
    if job == ("yes"):
        job = input("Enter your job title: ")
    elif job == ("no"):
        job = ("I don't have a job.")
    personal_details[name] = age, address, birthday, email, job
    print(personal_details)
    break

