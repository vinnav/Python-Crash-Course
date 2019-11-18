
ProgrammingPoll = "ProgrammingPoll.txt"

with open(ProgrammingPoll, "a") as file_object:
    while True:
        answer = input("Why do you like programming? (\"quit\" to quit): ")
        if answer.lower() != "quit":
            file_object.write(f"\n{answer}")
            print("Answer added to the poll")
        else:
            print("Programming Poll completed!")
            break
    