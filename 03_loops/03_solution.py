#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 3
for i in range(1, 11):
    if i == 5:
        continue                    #it will extract or skip the part or iteration, that u have mentioned to skip. e.g here u have mentioned to skip 5th one .
    print(number, 'x', i, '=', number * i)
    
#ans: it will print all the number except 5th one     
    

##Problem: Print the multiplication table for a given number up to 10.

number = int(input("Enter the Number: "))
for i in range (1, 11):
    print(number, "x", i, "=", number*i)

#Ans:
#Enter the Number: 9
# Then it will give u the 9th table 