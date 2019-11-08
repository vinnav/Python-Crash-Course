favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_polling = ["jen", "vin", "phil", "ale"]

for people in people_polling:
    if people in favorite_languages.keys():
        print(f"Thank you for taking the poll, {people.title()}")
    else:
        print(f"Can you please take the poll, {people.title()}?")