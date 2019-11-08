favourite_places = {
    "Vin" : ["Rome", "Athens", "Berlin"],
    "Ale" : ["London"],
    "Mario" : ["Palermo", "Malta"],
}

for person in favourite_places:
    print(f"\n{person}'s favourite places:")
    for place in favourite_places[person]:
        print(place)