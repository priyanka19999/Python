#Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


#Encapsulation
class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel
        
    def get_brand(self):
        return self.__brand + " !"
my_car = Car("Toyota", "Corolla")
print(my_car.__brand)  #AttributeError: 'Car' object has no attribute '__brand'
print(my_car.get_brand())

#The double underscore (__) makes the attribute private (name mangling).