username = "priyanka"

def fun():
    username = "chai"
    print(username) #print variable within the function scope

print(username) # global scope
fun()

#ans: 
# priyanka
#chai

#Ex-2
x = 99
def func(y):
    z = x + y
    return z
result = func(1)
print(result) #ans: 100

#Ex-3(global value override)
x = 99
def func2():
    global x
    x = 88
func2()
print(x) #ans: 88


#Ex-4

x = 95
def f1():
    x = 89
    def f2():
        print(x)
    return f2  
my_res = f1()
my_res() # ans : 89



#Ex: 5
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual


f = chaicoder(2)
g = chaicoder(3)

print(f(3)) #ans: 9
print(g(3)) #ans: 27