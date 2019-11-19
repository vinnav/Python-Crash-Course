import json

favouriteNumber = input("Choose favourite number: ")

with open("number.json", "w") as f:
    json.dump(favouriteNumber, f)
