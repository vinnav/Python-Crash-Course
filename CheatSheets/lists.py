listExample = ["element0", "element1", "element2", "element3"]

listExample[0] = "element0"         # First element of the list
listExample[-1] = "element3"        # Last element of the list

# Changing, adding, removing elements

listExample[0] = "new_element0"     # Change element 0
listExample.append("element4")      # Append element to the end of the list
listExample.insert(0, "inserted")   # Insert element at position 0
del listExample[0]                  # Remove element at position 0 
popped_element = listExample.pop()  # Assign removed element from end of the list
popped_element = listExample.pop(0) # Same as .pop but at position 0

listExample.remove("element1")      # Remove by value (only the first instance 
                                    # of the element, unless you use loop)

# Organize a list

listEx = ["b", "a", "t", "s"]
listEx.sort()                       # Sort in alphabetical order                 
listEx.sort(reverse=True)           # Reverse alphabetical order
print(sorted(listEx))   # Diplay the sorted list without affecting the order

listEx.reverse()                    # Reverse the list order
len(listEx)                         # Find the length of the list, starts from 1

# Loop through a List

cats = ["Mario", "Luke", "Bob"]
for cat in cats:                    # Loop through each element
    print(cat)

for value in range(1, 5):           # Loop through values in range, printing 1...4
    print(value)https://github.com/vinnav/Python-Crash-Course.git
for value in range(5)               # Loop printing 0...4

numbers = list(range(1, 6))         # Create the list [1, 2, 3, 4, 5]

even_numbers = list(range(2,11,2))  # The third value is the step size

# Statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits) = 0
max(digits) = 9
sum(digits) = 45

# List comprehension
squares = [vualue**2 for value in range(1, 11)]     # Generate a list in one line
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            # [expression to generate values, for loop to feed values]

# Slice a list
listExample[0:3]    # elements 0, 1, 2
listExample[:3]     # starts at the beginning
listExample[3:]     # goes to the end
listExample[-3:]    # last 3 elements

# Loop through a slice
for i in listExample[2:]:
    print(i)

# Copy a list
listExample2 = listExample[:]   # Copy the full list, without [:] you refence the list



