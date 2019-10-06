# This program is demonstrating the checking 
# of a palindrom number.
# Which means that if the last and the first
# digit are changed with each other the number
# remains the same.
# 
# For ex: 121 is a palindrome
# 		  123 is not a palindrome


a = str(input("Enter a number of three digits : "))

if(len(a) == 3):
	if(a[0] == a[2]):
		print("The number is palindrome")

	else: print("The number is not palindrome")

else:
	print("Number is not of three digits")