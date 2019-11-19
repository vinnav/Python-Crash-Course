import json
with open("number.json") as f:
    favouriteNumber = json.load(f)     

print(f"Your favourite number is {favouriteNumber}")