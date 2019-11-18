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

# Inheritance
class childClass(parentClass):                 # Electric car is a child of class Car
    def __init__(self, att1, att2, att3):
        super().__init__(att1, att2, att3) # Super() calls a method from parent Class
        self.att4 = "new attribute"
    
    def parentMethod(self):             # Override a parent method by giving the child
        print()                         # method the same name

child = childClass("att1", "att2", "att3")

# Using a class as an attribute for another Class
class att4:
    def __init__(self, att4="att4"):
        self.att4 = att4
    
    def describeAtt4(self):
        print(f"{att4}")

class childClass(parentClass):                 
    def __init__(self, att1, att2, att3):
        super().__init__(att1, att2, att3) 
        self.att4 = att4()              # Create an istance of att4 class and assign it
    
child = childClass("att1", "att2", "att3")
child.att4.describeAtt4()               # Call method of att4 class

# Importing Classes
from car import Car                     # Import the class Car from car.py
from car import Car, ElectricCar        # Import multiple classes
import car                              # Import the full file
from car import *                       # It's against best practices because it could
                                        # create conflict with same name classes


