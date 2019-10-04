
string = "A Very Nice String"

#indexing single value
single_value = string[7]
print(single_value) # "N" 

#slicing from [start : end]
slice1 = string[2:11]
print(slice1) # "Very Nice"

#from start until the index (not included)
slice2 = string[:6]
print(slice2) # "A Very"

#from index until the end
slice3 = string[7:]
print(slice3) # "Nice String"

#from index until the third from the last
slice3 = string[7:-3]
print(slice3) # "Nice Str"

#index 0 to 10 with step of size 2
slice4 = string[0:10:2]
print(slice4) # "AVr i"

#index 2 until the end, if step of size 3
slice5 = string[2::3]
print(slice5) # "Vyi rg"

#from start to end, but backwards
slice6 = string[::-1]
print(slice6) # "gnirtS eciN yreV A"

#all slices works with array types as well
integers   = [0,1,2,3,4,5,6,7,8,9,10]
only_pairs = integers[0::2]
only_odds  = integers[1::2]
print( only_pairs ) # [0, 2, 4, 6, 8, 10]
print( only_odds ) # [1, 3, 5, 7, 9]

#You can make slices with the 'slice' function
middle        = slice(3, 6, None)
middle_values = integers[ middle ] # same as integers[3:6]
print(middle_values) # [3, 4, 5]