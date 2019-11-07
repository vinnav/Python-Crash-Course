locations = ["Tokyo", "Sydney", "Paris", "Berlin", "Peking"]

print("The list:")
print(locations)

print("The sorted list:")
print(sorted(locations))

print("The original list:")
print(locations)

print("The reverse sorted list:")
print(sorted(locations, reverse=True))

print("The original list:")
print(locations)

print("The reversed list:")
locations.reverse()
print(locations)

print("The original list:")
locations.reverse()
print(locations)

print("The sorted list:")
locations.sort()
print(locations)

print("The reverse sorted list:")
locations.sort(reverse=True)
print(locations)