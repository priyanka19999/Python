# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# Polymorphism
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, userbrand, usermodel):
        super().__init__(userbrand, usermodel)
          
    def fuel_type(self):
        return "Electric Charge"
    

tesla = ElectricCar("Tesla", "model S")
print(tesla.fuel_type()) #Electric Charge
 
    
safari = Car("Tata", "Safari")
print(safari.fuel_type()) # ans: Petrol or Diesel