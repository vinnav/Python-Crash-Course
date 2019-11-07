# Changing case in a string with methods
name = "vin nav"
name.title() = "Vin Nav"
name.upper() = "VIN NAV"
name.lower() = "vin nav"

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

