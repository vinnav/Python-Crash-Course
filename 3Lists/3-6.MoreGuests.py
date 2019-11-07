guests = ["Einstein", "Elon Musk", "Napoleon"]

print(f"Would you like to come for dinner, Mr. {guests[0]}?")
print(f"Would you like to come for dinner, Mr. {guests[1]}?")
print(f"Would you like to come for dinner, Mr. {guests[2]}?")

print("\nOh.. I found a bigger dinner table!\n")

guests.insert(0, "Pitt")
guests.insert(2, "Obama")
guests.append("Bush")

for i in range(0, len(guests)):
    print(f"Would you like to come for dinner, Mr. {guests[i]}?")

print("\nOh.. I can only invite two people!\n")

for i in range(0, len(guests)-2):
    print(f"I'm sorry, you're not invited anymore, Mr. {guests[-1]}...")
    guests.pop()

for i in range(0, len(guests)):
    del guests[0]

print(guests)