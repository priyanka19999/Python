#Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
    
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar(Battery, Engine):
    pass

Audi = ElectricCar("Audi" , "A4")
print(Audi.battery_info())#this is battery
print(Audi.engine_info())#this is engine
print(Audi.model)#A4
print(Audi.brand) #Audi