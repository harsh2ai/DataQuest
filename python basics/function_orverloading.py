# This program will demonstrate the 
# Function overloading in python.
# That simple means that a same function performing 
# different task with different parameters passed to it.

# Here the area when passed with one parameter gives area of circle
# but gives are of rectangle when provided with two parameters.

class overloading:

	def area(self, l, w = None):
		if (w == None):
			print("The area of Circle is:",2* 1.414 * l)
		else:
			print("The area of Rectangle is: ",l*w)



# Demonstaration.
a = overloading()
a.area(16)
a.area(2,2)