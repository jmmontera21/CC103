#Create a python function that will accept  a person's name and age, address, birthdate, email, if he/she has a job, what is the job title, and put all those data in a dictionary, and then will ask the user if he/she want to continue the program, if the user opted 'yes' then the the user will have to fill out again name etc., program loop will only halt/stop if user opted 'no'. Lastly the program will need to display/print all the data that was stored.

print("\t\t ********************")
print("\t\t Personal Details v.2")
print("\t\t ********************")
print("\t")

personal_details = {}
def biodata(list):
    return sum(list)/len(list)
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

    personal_details[name]= age, address, birthday, email, job

    additional = input("Do you want to add another set of information?""(yes/no)")
    if additional == "no":
        break
    else:
        continue

print("\n")
print("This is all the information you have generated: \n")
print(personal_details)
