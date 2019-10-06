"""
Author : Alok kumar

*args:

When a function parameters starts with asterik, it allows arbitrary number of arguments,
and the function takes them as tuple of values.
"""

def args_example(*args):
    return sum(args)*0.05

print(args_example(40,60,20))

"""
**kwargs:

Similarly, python offers a way to handle arbitrary number of keyword arguments.
Double asterik is used to accept arbitrary number of keyword arguments.
"""

def kwargs_example(**kwargs):
    if 'car' in kwargs:
        print(f"My favourite car is {kwargs['car']}")
    else:
        print("I don't like driving cars")

kwargs_example(car='Honda',fruit='mango')

"""
Note args and kwargs are just conventional names you can use any name inplace of it.
"""
