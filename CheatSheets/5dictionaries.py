# A dictionary is a collection of key-value pairs
dictExample = {"color": "green", "points": 5}
print(dictExample["color"])         # Access the key "color", gives value "green"
dictExample["newKey"] = "newValue"  # Assign a new key-value pair
del dictExample["points"]           # Remove a key-value pair

dictEx2 = {                    # A dictionary on several lines
    "width" : 25,
    "heigth" : 10,
    "color" : "red",
    "shape" : "rectangle",
}

print(dictEx2["material"])     # Return error "KeyError" if "material" doesn't exist
dictEx2.get("material", "default")  # Return "material" value, or default if missing
                                    # if only the first argument, default is None

# Looping through a dictionary
for key, value in dictEx2.items():  # Loop through all key-value pairs
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in dictEx2.keys():          # Loop through all the keys 
    print(key)
for key in dictEx2:                 # Looping through keys is the default behaviour
    print(key)

for sortedKey in sorted(dictEx2):   # Loop through a sorted dictionary
    print(sortedKey)

for value in dictEx2.values()      # Loop through all the values

for value in set(dictEx2.values()) # Loop through a list of non-repetitive values

setEx = {"a", "b", "c"}  # A set is a list of non-repetitive values, it doens't
                         # retain items in any specific order

# Nesting
listEx = [dictEx, dictEx2] # A list of dictionaries

dictEx 3 = {               # A list in a dictionary
    "key" = "value",
    "list" = ["value1", "value2"],
}

users = {                  # A dictionary of dictionaries
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}