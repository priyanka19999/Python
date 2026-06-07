#Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.__model = usermodel

    @property
    def model(self):
        return self.__model
    
my_car = Car("Tata", "Safari")
my_car.model = "City" #You can also control modifications: property 'model' of 'Car' object has no setter 
safariTwo = Car("Tata" , "Nexon")
print(my_car.model) #Safari



#  @property 
# ->It provides controlled access to private attributes.
# Users can read model, but they cannot directly access __model