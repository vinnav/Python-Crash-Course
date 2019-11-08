vin = {
    "first_name" : "Vincenzo",
    "second_name" : "Navarra",
    "age" : "30",
    "city" : "Rome",
}

ale = {
    "first_name" : "Alessio",
    "second_name" : "Navarra",
    "age" : "30",
    "city" : "Stansted",
}

bob = {
    "first_name" : "Bob",
    "second_name" : "Ross",
    "age" : "55",
    "city" : "New York",
}

people = [vin, ale, bob]

for person in people:
    print(f"\nAll I know about {person['first_name']}:")
    for k, v in person.items():
        print(f"{k} = {v}")
