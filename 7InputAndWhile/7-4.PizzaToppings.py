while True:
    topping = input("Enter the chosen topping (enter 'quit' to exit): ")
    if topping.lower() == "quit":
        break
    print(f"{topping} will be added to your pizza!")
