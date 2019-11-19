sum = 0
while True:
    number = input("Select number to add: ")
    try:
        sum += int(number)
    except ValueError:
        pass
    else:
        print(f"The sum is {sum}")