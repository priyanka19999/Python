#Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "User"):
    return "Hello, " + name + " !"
print(greet("pri"))
#ans: Hello, pri !

#If no value is passed, name defaults to "User" 
#If you call the function without an argument: 
print(greet())

#Ans:Hello, User !