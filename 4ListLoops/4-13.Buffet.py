foods = ("rice", "chips", "pork", "chicken", "watermelon")

for food in foods:
    print(food)

# foods[2] = "pasta"    doesn't work, can't change element in a tuple

foods = ("rice", "pasta", "ravioli", "chicken", "watermelon")

print('\nNew foods in the Buffet')
for food in foods:
    print(food)