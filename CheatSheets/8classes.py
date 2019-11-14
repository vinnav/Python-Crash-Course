class Dog:                              # The name of the class is capitalized
    """A model of a dog"""

    def __init__(self, name, age):      # Method run on the class creation
        """Initialize name and age attributes"""
        self.name = name                # The prefix "self" makes the variable available
        self.age = age                  # to every method of the class, and make them
                                            # accessible from instances of the class
        self.tricks = 0                 # A default attribute
    def sit(self):                      # self means the method doens't need parameters
        """Simulate a dog sitting on command"""
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        """Simulate rolling over on command"""
        print(f"{self.name} rolled over")

    def updateTricks(self, newTricks):  # Method to change tricks attribute
        self.tricks = newTricks
    
    def addTrick(self, addedTricks):    # Method to add tricks attribute
        self.tricks += addedTricks

# Making an instance from a Class
my_dog = Dog("Bob", 5)
print(f"My dog name is {my_dog.name}")
my_dog.sit()

# Changing an attribute
my_dog.tricks = 3                       # Change the attribute directly (now 3)
my_dog.updateTricks(4)                  # Through a method (now 4)
my_dog.addedTricks(2)                   # Add tricks (now 6)
