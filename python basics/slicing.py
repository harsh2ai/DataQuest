# you can slice a list, tuple or array natively within python
# array's are created with libraries such as numpy and the same rules apply but no examples given
# slicing a list example
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # stores list as variable "example_list"

# [start,stop,step]
print(example_list[1:4])  # [2,3,4]

# start defaults to 0 when omitted
# step defaults to 1 when omitted
print(example_list[:4])  # [1,2,3,4]
print(example_list[::2])  # [1, 3, 5, 7, 9]

# you can start at the end by making the step negative
print(example_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# slicing a tuple works in the same way
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # stores tuple as variable "example_tuple"

# [start,stop,step]
print(example_tuple[1:4])  # (2,3,4)

# start defaults to 0 when omitted
# step defaults to 1 when omitted
print(example_tuple[:4])  # (1,2,3,4)
print(example_tuple[::2])  # (1, 3, 5, 7, 9)

# you can start at the end by making the step negative
print(example_tuple[::-1])  # (9, 8, 7, 6, 5, 4, 3, 2, 1)

# it is also possible to use python slice objects
slice_object = slice(1, 3)
print(example_list[slice_object])   # [2, 3]

