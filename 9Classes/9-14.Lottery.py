from random import choice

lottery = ["a", "b", "c", "d", "e", 1, 2, 3, 4, 5]
winner = choice(lottery)
print(f"The winner is: {winner}")
times = 1

while True:
    ticket = choice(lottery)
    print(f"We got ticket number: {ticket}")
    if ticket == winner:
        print(f"You won with ticket: {ticket} in {times} attempts.")
        break
    lottery.remove(ticket)
    times += 1
