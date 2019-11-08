current_users = ["Vin", "Ale", "Mario", "Fabio", "Admin"]
current_users_lower = ["vin", "ale", "mario", "fabio", "admin"]
new_users = ["Bob", "Ross", "Mario", "Fabio", "Mel"]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry {user}, you will need to enter a new username!")
    else:
        print(f"Nice, the username {user} is still available")