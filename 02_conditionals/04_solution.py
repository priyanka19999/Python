#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
fruit = "Banana"
color = "yellow"

if fruit == "Banana":
    if color == "Green":
        print("unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
    else:
        print("Invalid/ Unknown condition ")
        
# ans: Ripe