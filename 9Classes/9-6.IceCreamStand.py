class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} dishes")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Pistacho"]
    
    def diplayFlavors(self):
        print("These are the restaurant flavors:")
        for flavor in self.flavors:
            print(f"\t {flavor}")

iceRisto = IceCreamStand("Geloh", "iceCreams")
iceRisto.describe_restaurant()
iceRisto.diplayFlavors()