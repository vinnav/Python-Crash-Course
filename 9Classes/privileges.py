class User:
    def __init__(self, firstName, lastName, location, theme="Black"):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location
        self.theme = theme
    
    def describeUser(self):
        print(f"The user {self.firstName} {self.lastName} is based in {self.location} and has chosen the theme {self.theme}")
    
    def greetUser(self):
        print(f"Hi {self.firstName} {self.lastName}! How are you?")

class Privileges:

    def __init__(self):
        self.privileges = ["Can Add Post", "Can Delete", "Can ban user"]
    
    def showPrivileges(self):
        print("The Admin has this privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    def __init__(self, firstName, lastName, location, theme):
        super().__init__(firstName, lastName, location, theme)
        self.privileges = Privileges()

