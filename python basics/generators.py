"""
Generator function allows us to write  a function that can send back a value and 
then later resume to pick up where it left off. In most aspects, a generator function will appear very similar
to a normal fucntion. The main difference is when a generator function is complied they 
become an object that supports an iteration protocol.
"""
import math

# Generator function to find sqaure root of a number
def gensqrt(n):
    for num in range(n):
        yield math.sqrt(num)

# Calling the generator function

for x in gensqrt(10):
    print("{0:.2f}".format(x))

