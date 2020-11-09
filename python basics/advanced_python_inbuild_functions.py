# Author: Alok kumar
# Created on: 10/07/19
"""
1.map()
map() is a build-in Python function that takes in two or more arguments and returns
an iterator.
"""

# Function to convert celsius to fahrenheit
def fahrenheit(celsius):
    return (9/5)*celsius + 32

tempratures = [0,22.5,40,100]

F_tempartures = map(fahrenheit,tempratures)

print(list(F_tempartures))

"""
2.reduce()
An inbuild python fucntion that applies the function to the sequence. 
It then returns a single value
"""
from functools import reduce
lst = [47,11,42,13]
print(reduce(lambda x,y: x+y, lst))

"""
3.filter()
This function filter out all the elements of an iterable, for which the 
function returns True. This function needs a function a function as its first argument.
"""

def even_check(num):
    if num%2 == 0:
        return True

lst = range(20)

print(list(filter(even_check,lst)))

"""
4.zip
This is an inbuild python function which makes an iterator that aggregates elements
from each of the iteratbles.
"""

x = [1,2,3]
y = [4,5,6]

print(list(zip(x,y)))

"""
5.enumerate()
This function allows to keep a count as we iterate through an object. It returns a 
tuple in form(count,element). The function itself is equivalent to

def enumerate(sequence, start = 0):
    n = start
    for elem in sequence:
        yield n, elem
        n+=1
"""

lst = ['a','b','c']

for number, item in enumerate(lst):
    print(number)
    print(item)

"""
6.all() and any()
all() and any() are built-in-functions in python that allow us to conveniently check
for boolean matching in an iterable. all() will return True if all elements in an iterable
are True.any() will return True if any of the elements in the iterable is True.
"""

lst = [True,True,False,True,5>0]
print(all(lst))
print(any(lst))

lst = [3>0,True,6==6]
print(all(lst))
print(any(lst))

"""
7.complex()
complex() returns a complex number with the value real + imag*1j or converts a 
string and number to a complex number
"""

print(complex(2,3))
print(complex('12+2j'))


