#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

#1st way
pet = "dog"
age = 8
if pet == "dog" and age < 2:
    food = "puppy food"
elif  age > 5:
    food = "Senior dog food"
else:
    food = "In between 2-5 yrs food"
    
print(food) #Senior dog food

if pet == "cat" and age < 2:
    food = "cat food"
elif age > 5:
    food = "Senior cat food"
else:
    food = "In between 2-5 yrs food"

print(food)

#Answe: Senior cat food
