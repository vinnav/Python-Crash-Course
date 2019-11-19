number1 = input("Select first number: ")
number2 = input("Select second number: ")
try:
    sum = int(number1) + int(number2)
except ValueError:
    print("You must input numbers!")
else:
    print(f"The sum is {sum}")