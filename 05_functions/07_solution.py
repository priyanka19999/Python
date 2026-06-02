#Problem: Write a function that takes variable number of arguments and returns their sum.
def sum_all(*args):
    print(args)
    for i in args:     # doubles the number
        print(i*2)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9))


#Ans:
# (1, 2)
# 2
# 4
# 3
# (1, 2, 3, 4, 5)
# 2
# 4
# 6
# 8
# 10
# 15
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 45