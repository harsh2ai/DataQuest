number = 0

for number in range(10):
    print('Number is ' + str(number))
print('\n\n')


#using break statement 

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')


#using pass statement

for number in range(10):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop')
print('\n\n')


#using continue statement 

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')

