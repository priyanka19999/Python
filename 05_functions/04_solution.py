#Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_stats(radius):
   area = math.pi * radius ** 2
   circumference =  2 * math.pi * radius
   return area, circumference

a, c = circle_stats(3)
print("Area: ", a , "Circumference: ", c)
# Ans: Area: 28.274333882308138 Circumference:  18.8495559215387

#for round off digit
print("Area: ", round(a, 2) , "Circumference: ", round(c, 2)) 
# used round(number, ndigits) 
#number → The number to round.
#ndigits (optional) → Number of decimal places to keep.
#ans:Area:  28.27 Circumference:  18.85
