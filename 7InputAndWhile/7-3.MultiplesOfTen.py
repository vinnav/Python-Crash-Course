number = input("I'll tell you if your number is a multiple of ten.\nInsert number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")