#Problem: Check if a number is prime.

number = 29
is_prime = True

if number > 1:
    for i in range (2, number):
        if (number % i) == 0:
            is_prime = False
            break
print("number is a prime number:", is_prime)

#Ans: number is a prime number: True