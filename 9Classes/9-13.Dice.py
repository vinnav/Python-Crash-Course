from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)

newDie = Die()
for i in range(1,10):
    result = newDie.roll_die()
    print(f"Dice roll: {result}")

newDie10 = Die(10)
for i in range(1,10):
    result = newDie10.roll_die()
    print(f"10 Dice roll: {result}")

newDie20 = Die(20)
for i in range(1,10):
    result = newDie20.roll_die()
    print(f"20 Dice roll: {result}")
