class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car ha {self.odometer_reading} miles on it")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
tesla = ElectricCar("Tesla", "Model S", 2019)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()