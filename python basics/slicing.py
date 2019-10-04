# Slicing can be done by using the `[]` notation or built in 'slice()' method on any data type that uses indexing (strings, lists, etc)
# The normal usage would be with the square brackets
# The full syntax [start:stop:step] 
test_string = 'Hacktoberfest'
test_list = ['Hacktoberfest', 'is', 'so', 'freaking', 'awesome']

# Grabbing value at regular index
print(test_string[2]) # Returns 'c'
print(test_list[2]) # Returns 'so'

# [start:stop] will return values by the index range given inclusively (does not include the value at stop index)
print(test_string[1:3]) # Returns 'ac'
print(test_list[1:3]) # Returns ['is', 'so']

# If you add a step, then it will only return every n-th item
print(test_string[::2]) # returns 'Hctbret'
print(test_list[::2]) # returns ['Hacktoberfest', 'so', 'awesome']

# You could even do negative values! It essentially works backwards
print(test_string[-1]) # Returns 't'
print(test_list[-1]) # Returns 'awesome'

# You can reverse the string/list as well by passing in a negative number for the step
print(test_string[::-1]) # Returns 'tsefrebotkcaH'
print(test_list[::-1]) # Returns ['awesome', 'freaking', 'so', 'is', 'Hacktoberfest']