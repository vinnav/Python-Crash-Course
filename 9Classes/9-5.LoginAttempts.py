class User:
    def __init__(self, firstName, lastName, location, theme="Black"):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location
        self.theme = theme
        self.loginAttempts = 0
    
    def describeUser(self):
        print(f"The user {self.firstName} {self.lastName} is based in {self.location} and has chosen the theme {self.theme}")
    
    def greetUser(self):
        print(f"Hi {self.firstName} {self.lastName}! How are you?")

    def incrementLoginAttempts(self):
        self.loginAttempts += 1

    def resetLoginAtttemps(self):
        self.loginAttempts = 0

vin = User("Vincenzo", "Navarra", "Italy", "Pink")

vin.incrementLoginAttempts()
vin.incrementLoginAttempts()
vin.incrementLoginAttempts()
print(f"Vin login attempts: {vin.loginAttempts}")

vin.resetLoginAtttemps()
print(f"Vin login attempts: {vin.loginAttempts}")

