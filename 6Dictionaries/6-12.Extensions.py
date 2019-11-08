cities = {
    "Rome" : {
        "Country" : "Italy",
        "Population" : "4 Million",
        "Fact" : "Center of the Roman Empire",
    }, 
    "London" : {
        "Country" : "Uk",
        "Population" : "9 Million",
        "Fact" : "Has jellied eels",
    },
    "Mumbai" : {
        "Country" : "India",
        "Population" : "18 Million",
        "Fact" : "Home of Bollywood",
    },
    "Tokyo" : {
        "Country" : "Japan",
        "Population" : "9 Million",
        "Fact" : "Has animes",
    },
    "Paris" : {
        "Country" : "France",
        "Population" : "10 Million",
        "Fact" : "Has the Tour Eiffel",
    },
}

for city in cities:
    print(f"{city} data:")
    for k, v in cities[city].items():
        print(f"{k} : {v}")
    print()