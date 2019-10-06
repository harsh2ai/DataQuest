# This program demostrate the following:
# - Creation of array in python
# - Inserting values in array
# - Changing values in array at particular index

# Creating a 1D Array
a = []

# Inserting Values in array using for loop
def insertVal(num_of_values):
	for i in range(0, num_of_values):
		a.append(input("Enter the Number: "))

	print(a)

# Inserting Value at a particular index
def insertAt(val, index):
	print("Changing value at {} index with {}".format(index, val))
	if(index+1 > len(a)):
		print("Invalid Index!")
	else:
		a[index] = val

	print(a)

# Inserting value at the end of the array
def add(val):
	print("Adding {} at the end of the Array".format(val))
	a.append(val)

	print(a)


# Demostration...
insertVal(6)
insertAt(3, 2)
add(66)