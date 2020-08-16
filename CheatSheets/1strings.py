# Changing case in a string with methods
name = "vin nav"
name.title() = "Vin Nav"
name.upper() = "VIN NAV"
name.lower() = "vin nav"

# .format()
a = "one"
b = "two"
ab = "{} {}".format(a, b) # ab = "one two"
# align
"{:>10}".format("test") #  "      test"
"{:10}".format("test") #   "test      "
"{:.10}".format("test") #  "......test"
"{:^8}".format("test") #   "  test  "
"{d}{o}{X}{b}".format(10) # format 10 in decimal, octal, exadecimal, binary

# f-strings (format strings), put variables into strings, from Python 3.7
first_name = "vin"
last_name = "nav"
full_name = f"{first name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

# Whitespace
    # Add
tab = "\t"
newline = "\n"
    # Strip
name = " vin  "
name.strip() = "vin" # .rstrip or .lstrip for only right or left side whitspace

