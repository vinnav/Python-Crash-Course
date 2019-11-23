import json

try:
    with open("number.json") as f:
        favouriteNumber = json.load(f)     
    print(f"Your favourite number is {favouriteNumber}")
except FileNotFoundError:
    favouriteNumber = input("Choose favourite number: ")
    with open("number.json", "w") as f:
        json.dump(favouriteNumber, f)

