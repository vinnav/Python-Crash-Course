vacation = {}
activeFlag = True

while activeFlag:
    user = input("Input your name: ")
    place = input("If you could visit one place in the world, where would you go? ")

    vacation[user] = place
    repeat = input("Do you want to add other users? (y/n): ")
    if repeat.lower() == "n":
        activeFlag = False

for user, place in vacation.items():
    print(f"{user}'s favourite place is {place}.")

