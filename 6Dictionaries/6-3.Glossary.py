glossary = {
    "True" : "A boolean operator for truthy statements",
    "%" : "The modulo operator",
    "list" : "A group of values",
    "for" : "The keyword to start a loop",
    "dictionary" : "A group of key-value pairs",
}

print("THE GLOSSARY:")
for k in glossary:
    print(f"\n{k.title()}, {glossary[k]}")