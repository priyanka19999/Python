#Problem: Add a static method to the Car class that returns a general description of a car.
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
#Static method
    @staticmethod
    def general_description():
        return "Cars are means of Transport"

safari = Car("Tata", "Safari")
safariTwo = Car("Tata" , "Nexon")

print(Car.general_description()) #Ans:Cars are means of Transport