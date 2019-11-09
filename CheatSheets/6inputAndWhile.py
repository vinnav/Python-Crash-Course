# Input
var = input("prompt: ")     # Input example
int(var)                    # The input always gives a String

# While Loops
number = 0
while number < 5:           # While loop example
    print(number)
    number += 1
# Flag
flag = True                 # Flag example to stop a while loop
while flag:
    message = input()
    if message == "quit":
        flag = False
    else:
        print(message)
# Break
while True:                 # A loop that starts while True, will stop only if
    message = input()       # it reaches a break statement
    if message == "quit":
        break
    else:
        print(message)
# Continue
current_number = 0          # Continue ignore the rest of the loop and return to
while current_number < 10:  # the beginning
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# CTRL-C exit an infinite loop

# Lists and Dictionaries while loops
# List
listEx = [0, 1, 2, 2, 3]
while listEx:               # While runs until listEx is empty
    listEx.pop()

while 2 in listEx:          # .remove works for only one istance at a time
    listEx.remove(2)
# Dictionary
DictEx = {}
active = True
while active:
    key = input("Input key")
    value = input("Input value")
    DictEx[key] = value
    repeat = input("Do you want to repeat?")
    if repeat == "no":
        active = False
