#String manipulation
#Strings are "a list of characters", and here you can learn a bit of how to manipulate them.

string = "hello, world!"

#Capitalizes the first letter of the string.
print('Capitalize:', string.capitalize())

#Replaces a specific part of the string with another.
#In this case, it replaces every 'hello' with 'Greetings'
print('Replace:', string.replace('hello', 'Greetings'))

#Capitalizes the first letter of every word.
print('Title:', string.title())

#Turns every letter into upper case.
print('Uppercase:', string.upper())

#Now with a full-uppercase string.
string = 'HELLO, WORLD!'

#Turns every letter into lower case.
print('Lowercase:', string.lower())

#Now with extra spaces in the string.
string = ' hello, world! '

#Removes the extra spaces from left and right.
print('Strip:', string.strip())

#Removes the extra spaces from the right.
print('Right strip:', string.rstrip())

#Removes the extra spaces from the left.
print('Left strip:', string.lstrip())

#Splits the current string into a list of strings.
#In this case, every list element is separated from another when there's a comma in the original string.
#If no argument is given, it splits where it finds a blank space.
string_split = string.split(',')
print(string_split)

#After splitting, we can merge them together once more using join.
print('Join:', ''.join(string_split))

#Originally, join inserts a set of characters for every character in a string.
#You can use it to put - after every character, for example.
print('Separate characters:', '-'.join(string))

#Or to separate strings from a list of strings when joining them.
print('Separate strings:', '-'.join(string_split))

#Strings are "a list of characters", and you can access specific parts of a string just like a list.
string = 'Hello, world!'

#Returns the very first character of a string.
print('Position 0:', string[0])

#Returns from character in position 0 until character in position 4.
print('Position 0 to 4:', string[:5])
#Note it uses [:5], but it doesn't include position 5 in the output.

#Returns from character in position 7 until the end.
print('Position 7 to end:', string[7:])

#Returns from character in position 3 until character in position 5.
print('Position 3 to 5:', string[3:6])
#Just like the first example, it uses :6 but doesn't include position 6 in the output.

#Returns from character in position 3 until character in position 9, picking a character every 2 characters.
print('Position 3 to 8, every 2 characters:', string[3:9:2])
#As explained above, even though we use :9, the character in position 9 is not included in the output.

#The same way, we can pick a string for every character, but backwards.
print('Reversed:', string[::-1])
#Note we needed to put :: before -1 because the first two arguments are used for position, just like demonstrated above.

#Returns the position of a set of characters in a string
print('Position of "world!":', string.find('world!'))
#Note it returns only the position of the first character of what you're searching for.
#If there is more than one ocurrance of what you're searching for, it returns the first.

#If such set of characters is not found, it returns -1.
print('Position of "Hola!":', string.find('Hola!'))
