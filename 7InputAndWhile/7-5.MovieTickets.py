age = ""
while age == "":
    age = input("Insert your age: ")
    age = int(age)
    if age < 3:
        print("Your movie ticket is free")
    elif age > 3 and age < 12:
        print("The ticket is 10$")
    else:
        print("The ticket is 15$")
        