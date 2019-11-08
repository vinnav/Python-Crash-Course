rivers = {
    "nile" : "egypt",
    "amazon" : "brazil",
    "mississippi" : "usa",
}

print("Full sentence:")
for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")

print("\nList of rivers:")
for river in rivers:
    print(river.title())

print("\nList of Countries")
for value in rivers.values():
    print(value.title())