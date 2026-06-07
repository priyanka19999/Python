#Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


def debug(func):
    def wrapper(*args , **kwargs):
        args_value = ', '.join([str(arg) for arg in args])
        kwargs_value = ",".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"{func.__name__} with args {args_value} and kwargs{kwargs_value}")
        return func(*args , **kwargs)
    return wrapper


@debug
def Hello():
    print("Hello..!")
Hello()

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Joe", greeting="Hello !")

# Ans
# Hello with args  and kwargs
# Hello..!
# greet with args Joe and kwargsgreeting=Hello !
# Hello !, Joe