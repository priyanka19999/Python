#Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


distance = 5

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "car"
    
print("AI recommends you the transport of: ", transport)

# answer : AI recommends you the transport of:  Bike 
    

#2nd way (user input)

distance = int(input("Enter the distance"))

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "car"
    
print("Your mode of transportation is" , transport)

# here u have to give certain value in terminal as input and it will give u the answer according to the condition

#Enter the distance 50
# Your mode of transportation is car