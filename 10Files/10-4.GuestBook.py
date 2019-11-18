
guestBook = "guestBook.txt"

with open(guestBook, "a") as file_object:
    file_object.write(f"Book of people invited:")
    while True:
        guestName = input("You're invited to the party! Insert you name please (\"quit\" to quit): ")
        if guestName.lower() != "quit":
            file_object.write(f"\n\t{guestName}")
            print(f"Welcome to the party {guestName}")
        else:
            print("Guestbook completed!")
            break
            