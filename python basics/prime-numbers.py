# Python program to check if the input number is prime or not

# take input from the user
num = int(input("Please enter a number: "))

# prime numbers are greater than 1
if num > 1:
    for i in range(2, num): # check for factors
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
