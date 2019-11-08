# An expression that can be evaluated as True or False is called a
# Conditional Test

2 == 2
True

car = "Audi"
car.lower() == "audi"   # .lower() makes the test case insensitive
True

# Checks
==, !=, <,<=,>=,>

# Check multiple conditions

2 == 2 and 2 != 3
False

2 == 2 and 2 != 3
True

pizzas = ['margherita', 'capricciosa', 'pepperoni', 'mushrooms', 'ham']
"margherita" in pizzas  # Checks if value is in the list
True

"onions" not in pizzas # Check if value is not in the list
True

# If statements

number = 10
if number > 5:
    print("True")
elif number > 15:
    print("False")
else:
    print("False")

# Lists in If statements
listExample = []            # An empty list evaluate to False
if listExample:         
    print(listExample)
else:
    print("The list is empty")

# Check a list against another
list1 = [1, 3, 5, 7]
list2 = [1, 2, 3, 4, 5, 6, 7]

for number in list1:
    if number in list2:
        print(f"{number} is in list2")
    else:
        print(f"{number} is not in list2")