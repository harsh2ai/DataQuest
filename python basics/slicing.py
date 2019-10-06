
# lst contains all number from 1 to 10 
lst = range(1, 11) 
print lst 
#Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
#  below list has numbers from 2 to 5 
lst1_5 = lst[1 : 5] 
print lst1_5 
#Output : [2, 3, 4, 5]
  
#  below list has numbers from 6 to 8 
lst5_8 = lst[5 : 8] 
print lst5_8 
#Output : [6, 7, 8]
  
#  below list has numbers from 2 to 10 
lst1_ = lst[1 : ] 
print lst1_ 
#Output : [2, 3, 4, 5, 6, 7, 8, 9, 10]
  
#  below list has numbers from 1 to 5 
lst_5 = lst[: 5] 
print lst_5 
#Output : [1, 2, 3, 4, 5]
  
#  below list has numbers from 2 to 8 in step 2 
lst1_8_2 = lst[1 : 8 : 2] 
print lst1_8_2 
#Output : [2, 4, 6, 8]
  
#  below list has numbers from 10 to 1 
lst_rev = lst[ : : -1] 
print lst_rev 
#Output : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  
#  below list has numbers from 10 to 6 in step 2 
lst_rev_9_5_2 = lst[9 : 4 : -2] 
print lst_rev_9_5_2 
#Output : [10, 8, 6]
=======
# Slicing can be done by using the `[]` notation or built in 'slice()' method on any data type that uses indexing (strings, lists, etc).
# The normal usage would be with the square brackets.
# The full syntax is [start:stop:step].
test_string = 'Hacktoberfest'
test_list = ['Hacktoberfest', 'is', 'so', 'freaking', 'awesome']

# Grabbing value at regular index
print(test_string[2]) # Returns 'c'.
print(test_list[2]) # Returns 'so'.

# [start:stop] will return values by the index range given inclusively (does not include the value at stop index).
print(test_string[1:3]) # Returns 'ac'.
print(test_list[1:3]) # Returns ['is', 'so'].

# If you add a step, then it will only return every n-th item
print(test_string[::2]) # returns 'Hctbret'
print(test_list[::2]) # returns ['Hacktoberfest', 'so', 'awesome']

# You could even do negative values! It essentially works backwards
print(test_string[-1]) # Returns 't'.
print(test_list[-1]) # Returns 'awesome'.

# You can reverse the string/list as well by passing in a negative number for the step
print(test_string[::-1]) # Returns 'tsefrebotkcaH'
print(test_list[::-1]) # Returns ['awesome', 'freaking', 'so', 'is', 'Hacktoberfest']

# Example of [start:stop:step] together
print(test_string[0:4:2]) # returns 'Hc'
print(test_list[0:4:2]) # returns ['Hacktoberfest', 'so']

# Example of [:stop:]. It will return values up to stop
print(test_string[:3]) # returns 'Hac'. test_string[:3:] is the same, but last colon is not needed if a step is not provided.
print(test_list[:3]) # returns ['Hacktoberfest', 'is', 'so']. test_list[:3:] is the same, but last colon is not needed if a step is not provided.

# Example of [start::]. It will only return values starting at start
print(test_string[2:]) # returns 'cktoberfest'
print(test_list[2:]) # returns ['so', 'freaking', 'awesome']

# Example of [:stop:] with negative value. It will return values up to stop in reverse
print(test_string[:-3]) # returns 'Hacktoberf'.
print(test_list[:-3]) # returns [['Hacktoberfest', 'is'].

# Example of [start::]. It will only return values starting at start in reverse.
print(test_string[-2:]) # returns 'st'.
print(test_list[-2:]) # returns ['freaking', 'awesome'].
