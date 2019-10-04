"""This is example for describing work with tuple.

Author: mhrownaghi
Github Page: https://github.com/mhrownaghi
"""

# create a tuple
fruits = ("apple", "banana", "orange", "cherry")

# access to tuple's elements
print(fruits[0])  # print -> apple
print(fruits[1])  # print -> banana
print(fruits[2])  # print -> orange
print(fruits[3])  # print -> cherry
print(fruits[-1])  # print -> cherry
print(fruits[-2])  # print -> orange
print(fruits[2:4])  # print -> orange cherry
print(fruits[:3])  # print -> apple banana orange
print(fruits[2:])  # print -> orange cherry

# Tuples are ReadOnly
# fruits[0] = "tomato" # this will raise an error

grades1 = (10, 20, 15, 14)
grades2 = (5, 10, 7, 6)
print(grades2 < grades1)  # print -> True
print(grades1 > grades2)  # print -> True
print(grades1 == grades2)  # print -> False
print(grades1 != grades2)  # print -> True
# (grades1 <= grades2) == (grades1 == grades2 or grades1 < grades2)
print(grades1 <= grades2)  # print -> False
print(grades1 < grades2 or grades1 == grades2)  # print -> False
# (grades1 >= grades2) == (grades1 == grades2 or grades1 > grades2)
print(grades1 >= grades2)  # print -> True
print(grades1 > grades2 or grades1 == grades2)  # print -> True

(math, english, physics, sport) = grades1   # unpacking
print(math)  # print -> 10
print(english)  # print -> 20
print(physics)  # print -> 15
print(sport)  # print -> 14

numbers = (1, 2, 6, 2, 3, 4, 1, 4, 7, 2, 4, 2)
# Print the number of times the value 2 appears in the tuple:
print(numbers.count(2))  # print -> 4
# Search for the first occurrence of the value 7, and return its position:
print(numbers.index(7))  # print -> 8
