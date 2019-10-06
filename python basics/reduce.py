"""
The function reduce applies the function to the sequence. 
It then returns a single value
"""

# Implementation

from functools import reduce

lst = [47,11,42,13]

print(reduce(lambda x,y:x+y,lst))