#Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
   for i in range (2, limit+1, 2):
        yield i   # yield store the function and its state in the memory 

for num in even_generator(10):
    print(num)
    
# Ans:

# 2
# 4
# 6
# 8
# 10