sandwich_orders = ["reuben", "philly", "tuna melt"]
finished_sandwich = []

while sandwich_orders:
    making = sandwich_orders.pop()
    print(f"I made your {making.title()} sandwich")
    finished_sandwich.append(making)

print("\nThese are the sandwiches I made")

for sandwich in finished_sandwich:
    print(f"\t{sandwich.title()}")