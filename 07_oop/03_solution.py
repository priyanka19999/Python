#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
#Inheritance
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
        
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, userbattery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = userbattery_size
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")       

print(my_tesla.model) #Model S
print(my_tesla.full_name()) #Tesla Model S
print(my_tesla.battery_size) #85kWh