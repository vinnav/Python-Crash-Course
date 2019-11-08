usernames = ["Vin", "Ale", "Mario", "Fabio", "Admin"]

for username in usernames:
    if username == "Admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again!")