
''' Some examples of how to create and use Python lists'''

#In python a list can be defined by placing quoted strings or variables within square brackets
# Define an empty list

MY_LIST = []

# Define a list with two values

MY_LIST = ['cat', 'dog']

# Define a list using a variable rather than a string

PET1 = 'cat'
PET2 = 'dog'
MY_LIST = [PET1, PET2]

# Print the number of items in a list

print(len(MY_LIST))

# Print contents of a list, for this we will use a for loop

for x in MY_LIST:
    print(x)

# Entries in a list start at 0, by placing the index number in sqaure brackets
#  we can use or print an entry

# Print first entry in a list

print(MY_LIST[0])

# Print second entry in a list

print(MY_LIST[1])

# Using -1 as the index we can print the last item in a list

print(MY_LIST[-1])

# Use value of first entry as a variable

MY_VARIABLE = MY_LIST[0]

# Change the second entry of my list to a different pet

MY_LIST[1] = 'frog'

# We can add extra entries to a list by using the append method

MY_LIST.append('goldfish')

# And remove them with the pop method

MY_LIST.pop()

# It is even possible to add lists together

MY_FIRST_LIST = ['cat', 'dog']
MY_SECOND_LIST = ['rabbit', 'goldfish', 'frog']

MY_COMBINED_LIST = MY_FIRST_LIST+MY_SECOND_LIST
