try:
    with open("cats.txt") as f:
        contents = f.read()    
except FileNotFoundError:
    print("cats.txt not found!")
else:
    print(contents)

try:
    with open("dogs.txt") as f:
        contents = f.read()    
except FileNotFoundError:
    print("dogs.txt not found!")
else:
    print(contents)            