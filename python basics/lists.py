# In python a list can be defined by placing quoted strings or variables within square brackets

# Define an empty list

my_list=[]

# Define a list with two values

my_list=['cat', 'dog']

# Define a list using a variable rather than a string

pet1='cat'
pet2='dog'
my_list=[pet1, pet2]

# Print the number of items in a list

print(len(my_list))

# Print contents of a list, for this we will use a for loop

for x in my_list:
    print(x)

# Entries in a list start at 0, by placing the index number in sqaure brackets we can use or print an entry
# Print first entry in a list

print(my_list[0])

# Print second entry in a list

print(my_list[1])

# Using -1 as the index we can print the last item in a list

print(my_list[-1])

# Use value of first entry as a variable

my_var=my_list[0]

# Change the second entry of my list to a different pet

my_list[1]='frog'

# We can add extra entries to a list by using the append method

my_list.append('goldfish')

# And remove them with the pop method

my_list.pop()

# It is even possible to add lists together

my_first_list=['cat', 'dog']
my_second_list=['rabbit', 'goldfish', 'frog']

my_combined_list=my_first_list+my_second_list


