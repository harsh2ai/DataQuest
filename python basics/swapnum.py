"""This program swaps the numbers that are stored in the variables a and b which are provided by the user at runtime"""

#Take two variables a and b and ask for user input
a=int(input("Enter a"))

b=int(input("Enter b"))
#Print the current values of variables

print("a=",a," b=",b)

#Swap the numbers
#t is used as a temporary storage variable
t=a
a=b
b=t
#Print the updated values of variables

print("a=",a," b=",b)
