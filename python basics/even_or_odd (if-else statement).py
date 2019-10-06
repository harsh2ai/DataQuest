# This program demostrate if-else statement
# in python.
# In this program we will see how to check
# whether a number is even or odd

# Taking input from user
num = int(input("Enter a number: "))

# Checking whether num is divisible by 2 or not.
# Here `%` gives the remender after dividing num by 2
# if remender is 0 i.e., num is divisible by 2 then its even
# So when condition gets `True` if-block runs, other wise else-block
# will run.

if ((num % 2) == 0):
	# Printing statement when condition is `true`
	print("Number is Even")

else:
	# Printing statement when condition is `false`
	print("Number is Odd")