sandwich_orders = ["reuben", "pastrami", "philly", "pastrami", "tuna melt", "pastrami"]
finished_sandwich = []

print("The Deli has run out of pastrami :(\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    making = sandwich_orders.pop()
    print(f"I made your {making.title()} sandwich")
    finished_sandwich.append(making)

print("\nThese are the sandwiches I made")

for sandwich in finished_sandwich:
    print(f"\t{sandwich.title()}")