try:
    with open("cats.txt") as f:
        contents = f.read()    
except FileNotFoundError:
    pass
else:
    print(contents)

try:
    with open("dogs.txt") as f:
        contents = f.read()    
except FileNotFoundError:
    pass
else:
    print(contents)            