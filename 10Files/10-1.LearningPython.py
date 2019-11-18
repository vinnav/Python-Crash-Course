# Print by reading the entire file
with open("learning_python.txt") as file_object:   # Opena a file and close it when not needed
    contents = file_object.read()       # Read from a file and assign its content
    print(contents)        

# Print by looping over the file object
with open("learning_python.txt") as file_object:   # Opena a file and close it when not needed
    for line in file_object:
        print(line.rstrip())

# Print by storing the line in a list
with open("learning_python.txt") as file_object:   # Opena a file and close it when not needed
    lines = file_object.readlines()
print()
for line in lines:
    print(line.rstrip())

