pizzas = ['margherita', 'capricciosa', 'pepperoni', 'mushrooms', 'ham']

friend_pizzas = pizzas[:]

pizzas.append('hawaian')
friend_pizzas.append('anchovies')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend\'s favourite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)