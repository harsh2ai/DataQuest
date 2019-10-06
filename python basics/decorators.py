"""
Author: Alok kumar
Date: 10/05/19
Decorators can be thought of as fucntions which modify the functionality of 
another function. They help to make our code shorter and more "pythonic"
"""

# Creating a Decorator

def new_decorator(func):

    def wrap_func():
        print("This line will be executed before the executing the function")

        func()

        print("This line will be executed after the function")
    return wrap_func

# Creating a function that needs decorator

def func_needs_decorator():
    print("This function needs a Decorator")

# Assigning a decorator to the function that needs decorator

func_needs_decorator = new_decorator(func_needs_decorator)

# Calling the decorated fucntion

func_needs_decorator()

# Decorator shorthand

# Python provides a shorthand for decorating a function with a decorator without 
# acutally reassign the function.

# Short hand for using decorators.
@new_decorator
def func_needs_decorator():
    print("This function needs a Decorator")

# Note internally @ operator performs the same assignment thing. It is just
# a syntactic sugar provided by python.

func_needs_decorator()