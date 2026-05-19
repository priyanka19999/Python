#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = 22
day = "wednesday"
price = 12 if age >= 18 else 8 #if age is greater than equal to 18 then price will be 12 , if not then price will be 8
if day == "wednesday":
    price = price - 2
    
print("Ticket price for you is $", price) #Ticket price for you is $ 10
