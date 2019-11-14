class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numberServed = 0
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} dishes")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def setNumberServed(self, setNumber):
        self.numberServed = setNumber
    
    def incrementNumberServed(self, incrementNumber):
        self.numberServed += incrementNumber

restaurant = Restaurant("Risto", "Italian")

print(f"Number served: {restaurant.numberServed}")

restaurant.numberServed = 3
print(f"Number served: {restaurant.numberServed}")

restaurant.setNumberServed(10)
print(f"Number served: {restaurant.numberServed}")

restaurant.incrementNumberServed(10)
print(f"Number served: {restaurant.numberServed}")
