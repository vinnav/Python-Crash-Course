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

vin = User("Vincenzo", "Navarra", "Italy", "Pink")
ale = User("Alessio", "Navarra", "Uk")
mar = User("Mario", "Pane", "Switzerland", "White")

vin.describeUser()
vin.greetUser()

ale.describeUser()
ale.greetUser()

mar.describeUser()
mar.greetUser()