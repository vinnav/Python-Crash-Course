# Function, a named block of code designed to do a particular task
def functionEx():           # Function example
    print("hello")

def functionEx2(user):       # A function can receive information through parameters
    print(f"Hello, {user}")  # The value "user" in functionEx2(user) is an argument

# ARGUMENTS
# Positional Arguments
def functionEx3(argument1, argument2):  # Order matters in positional arguments
    print(f"{argument1}, {argument2}")
functionEx3(1, 2)

# Keyword Arguments
def functionEx4(argument1, argument2):  # Order doesn't matter
    print(f"{argument1}, {argument2}")
functionEx4(argument2=2, argument1=1)

# Default Values
def functionEx5(argument1, argument2=2):# If the value is missing, it uses the default
    print(f"{argument1}, {argument2}")  # Parameters with default values must be
functionEx5(1)                          # listed after parameters with no default

# RETURN VALUES
def returningFunction(argument1, argument2):
    fullText = f"{argument1}, {argument2}"
    return fullText

# Dictionary
def album(name, title):
    album = {"artist": name, "album": title}
    return album                        # Return a Dictionary

# List
def listFunction(listEx):               # Loops through a list
    for element in listEx:
        print(element)
    
def moveList(listEx, listEx2):          # Moves a list to another
    while listEx:
        element = listEx.pop()
        listEx2.append(element)
moveList(listEx[:], listEx2)            # Gives as the first argument a copy of listEx
                                        # to keep the original listEx
# Arbitrary number of arguments
def functionEx6(*args):                 # It will make a tuple of arguments
    print(arguments)

def functionEx7(arg1, *args):           # After the first arg, the rest are arbitrary
    print(arguments)

def functionEx8(arg1, arg2, **kwargs):  # Arbitrary keyword arguments
    kwargs["key1"] = arg1
    kwargs["key2"] = arg2
    return kwargs                       # It will form a dictionary of arbirary keywords

functionEx8("key1": "value1"
            "key2": "value2"
            "key3": "value3")
# MODULES
# Import a module
import customModule                     # from customModule.py
customModule.function()                 # using a function from the module
from moduleName import functionName     # Import a specific function
from moduleName import functionName as fN # Give the function an alias
import moduleName as mN                 # Give the imported module an alias

from moduleName import *                # Import every function 
                                        # (no need to call moduleName.functioName)
# Style a function
def functionName(                       # Multi-line parameters
        parameter0, parameter 1,
        parameter2, parameter3):
    print()
