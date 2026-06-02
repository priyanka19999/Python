#Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwagrs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    
    
print_kwagrs(name = "shaktiman", power = "lazer")
print_kwagrs(enemy = "Dr. Jackaal")


#Ans:

# name : shaktiman
# power : lazer
# enemy : Dr. Jackaal