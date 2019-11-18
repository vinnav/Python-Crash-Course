with open("learning_python.txt") as file_object:   # Opena a file and close it when not needed
    lines = file_object.readlines()
print()
for line in lines:
    line = line.replace("Python", "C")
    print(line)