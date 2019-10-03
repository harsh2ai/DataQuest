"""
Basic comprehension about lists in Python and methods
"""

#create empty list
numbers = []

#Initialize with some values, or strings
numbers = [1, 2, 3]

#Inserting values at the end of the list with 'append' method
numbers.append('four')

"""
Or you can add a new value at a given position in list
The parameters of 'insert' are the position and the value
"""
numbers.insert(0, 'zero')

#You can print a list
print(numbers)

"""
You can remove an item if it's on the list by its value
(if its not on the list it will raise a ValueError)
"""
numbers.remove('four')

#Removing an item by its index
del(numbers[0])

#Count the occurences of a given value in the list
print(numbers.count(1))

#you can reverse the list
numbers.reverse()
print(numbers)

#if the list is unordered, you can sort it
numbers.sort()