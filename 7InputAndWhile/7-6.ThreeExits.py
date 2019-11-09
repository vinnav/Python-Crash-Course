# Conditional test
topping = ""
while topping != "quit":
    topping = input("Enter the chosen topping (enter 'quit' to exit): ")
    if topping != "quit":
        print(f"{topping} will be added to your pizza!")

# Active variable
active = True
while active:
    topping = input("Enter the chosen topping (enter 'quit' to exit): ")
    if topping.lower() == "quit":
        active = False
    else:
        print(f"{topping} will be added to your pizza!")

# Break Statement
while True:
    topping = input("Enter the chosen topping (enter 'quit' to exit): ")
    if topping.lower() == "quit":
        break
    print(f"{topping} will be added to your pizza!")
