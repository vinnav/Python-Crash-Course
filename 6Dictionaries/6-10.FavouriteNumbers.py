favourite_numbers = {
    "vin" : [7, 6, 4],
    "ale" : [3],
    "mario" : [5, 2, 3],
    "fabio" : [4, 3],
    "teo" : [9],
}

for person in favourite_numbers:
    print(f"\n{person}'s favourite number:")
    for number in favourite_numbers[person]:
        print(number)