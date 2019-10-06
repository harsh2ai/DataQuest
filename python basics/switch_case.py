# This program will demostrate the conversion of number to week-days using switch_case

# Here `num` will take the required input from user i.e, day number
num = int(input("Enter the Day Number: "))

# `switcher` is a dictionary which maps the user input to the required output.
# It happens in such a way that user input becomes a 'key' while answer as 'value'
switcher = {
	1: "Monday",
	2: "Tuesday",
	3: "Wednessday",
	4: "Thursday",
	5: "Friday",
	6: "Saturday",
	7: "Sunday",
}
	
# The actual value is search by the 'key' user provided using 
# `get()` method of dictionary.
# If number is not found the default output would be "Invalid Number", i.e., the 
# second input to get() method.
val = switcher.get(num, "Invalid Number !!")

# At the end printing the result
print("Week-day : ", val)
