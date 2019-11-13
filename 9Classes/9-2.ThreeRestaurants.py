class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} dishes")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Risto", "Italian")
restaurant2 = Restaurant("Style", "New Age")
restaurant3 = Restaurant("Raja", "Indian")


restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
