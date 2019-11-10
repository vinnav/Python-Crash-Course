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
def functionEx5(argument1, argument2=2): # If the value is missing, it uses the default
    print(f"{argument1}, {argument2}")   # Parameters with default values must be
functionEx5(1)                           # listed after parameters with no default

# RETURN VALUES
def returningFunction(argument1, argument2):
    fullText = f"{argument1}, {argument2}"
    return fullText
