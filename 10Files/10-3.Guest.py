guestName = input("You're invited to the party! Insert you name please: ")

guestList = "guestList.txt"

with open(guestList, "w") as file_object:
    file_object.write(f"List of people invited:\n\t{guestName}")