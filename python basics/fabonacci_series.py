# This program demostrate how to create a 
# Fabonacci Sequence - Akash Srivastava
# 0 1 1 2 3 5 8 13 ...

# Initial number for series
a = 0
b = 1

# taking input for number of Terms to be computed
num = int(input("Enter the number: "))

# if terms is 0, print 0
if (num == 0):
	print(0)

# if terms is 1, print 0 1
elif(num == 1):
	print(0, 1)

# if terms is num, do following
else:
	# print first two numbers
	print(a)
	print(b)
	# compute other numbers using for loop
	for i in range(0, num, 1):
		c = a + b
		print(c)
		a = b
		b = c 

