#Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

class ElectricCar(Car):
    def __init__(self, userbrand, usermodel):
        super().__init__(userbrand, usermodel)
my_tesla = ElectricCar("Tesla", "Model S") 

print(isinstance(my_tesla, Car)) #True
print(isinstance(my_tesla, ElectricCar)) #True


# isinstance() is a built-in Python function used to check whether an object belongs to a particular class