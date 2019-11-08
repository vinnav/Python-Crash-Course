meo = {
    "name" : "Meo",
    "animal" : "Cat",
}

doug = {
    "name" : "Doug",
    "animal" : "Dog",
}

pariot = {
    "name" : "Pariot",
    "animal" : "Parrot",
}

animals = [meo, doug, pariot]

for animal in animals:
    print(f"\nAll I know about {animal['name']}:")
    for k, v in animal.items():
        print(f"{k} = {v}")