def makeSub(*ingredients):
    print("\nThe sandwich has this ingredients: ")
    for ingredient in ingredients:
        print(f"\t-{ingredient}")

makeSub("Tomato", "Mozzarella")
makeSub("Chicken", "Pesto", "Blue Cheese")