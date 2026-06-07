#Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
        Car.total_car +=1

safari = Car("Tata", "Safari")
safariTwo = Car("Tata" , "Nexon")
print(Car.total_car) # Ans:2