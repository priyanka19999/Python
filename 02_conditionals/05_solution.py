#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

#1ST way
weather = "sunny"
activity = "Go for a walk"

if weather == "sunny":
    print("Go for a walk")
elif weather == "Rainy":
    print("Read a Book")
elif weather == "Snowy":
    print("Build a snowman")
#ans: Go for a walk

#2nd way 
weather = "sunny"
if weather == "sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a Book"
elif weather == "Snowy":
    activity = "Build a snowman"
print(activity) 

#ans: Go for a walk