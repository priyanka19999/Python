#Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

my_car = Car("Toyota", "Corolla")
print(my_car.brand) #Toyota
print(my_car.model) #Corolla

my_new_car = Car("Tata", "Safari")
print(my_new_car.model) #Safari


# __init__() is a special function that runs automatically whenever a new car is created.
#__init__ is a special method that runs automatically when an object is created.
#"self" helps Python know which object's data it should store or access.
# userbrand → brand given by the user
# usermodel → model given by the user
# self.brand → stores the brand inside that specific car
# self.model → stores the model inside that specific car