'''This is a simple game that will generate a random number between 1 and 100
and allow players to make a guess as to what that number will be.
The player will be allowed 5 guesses and each time the game will indicate
whether their last guess was higher or lower than the number they are trying to guess.
This program demonstrates for loops, inputs, the range function, conversion of string to integer
and conditional statements'''

# Import necessary libraries
import random

# Generate a random number between 1 and 100 and assign this to the 'target' variable
TARGET = random.randint(1, 100)

# Initialise the number of guesses so far at 0
GUESSES_SO_FAR = 0

# Display banner
print('//////////////////////')
print('Number guessing game')
print('/////////////////////')
print('')

# Setup permitted attempts as a range and loop through these
PERMITTED_ATTEMPTS = range(5)
for attempt in PERMITTED_ATTEMPTS:

    # Check user has not exceeded their maximum allowed guesses and loop until they have
    if GUESSES_SO_FAR < 5:
        # Prompt user for a guess and store as a variable 'guess', insert blank lines
        print('')
        guess = input('Please guess a number between 1 and 100 >> ')
        print('')
        # Convert guess from string to integer for logic, catch exceptions raised by bad syntax
        try:
            guess = int(guess)
        except SyntaxError:
            print('Please guess a number between 1 and 100.')
            print('')
            continue
        # Display congratulations message if guess matches target value
        if guess == TARGET:
            print('Well done, your guess is correct!')
            # Exit loop
            break
        # Display a warning if guess is out of permitted range
        if guess < 1 or guess > 100:
            print('Please guess a number between 1 and 100.')
        # Display an indication if guess is higher than target
        if guess > TARGET:
            print('Your guess is higher than the target number.')
        # Display an indication if guess is lower than target
        if guess < TARGET:
            print('Your guess is lower than the target number.')
        # Indicate if user is within 10 of target with their guess
        # There are two ways to do this in Python:
        # For ease of reading:
        # if guess > (TARGET - 10) and guess < (TARGET + 10) and guess != TARGET:
        # or...
        # by chaining comparison operators (preferred)
        if (TARGET - 10) < guess < (TARGET + 10) and guess != TARGET:
            print('Your guess is within 10 of the target value, you are doing great!')
        # Increment number of guesses, short syntax for guesses_so_far=guesses_so_far+1
        GUESSES_SO_FAR += 1
        # Check guesses remaining
        GUESSES_LEFT = 5 - GUESSES_SO_FAR
         # Exit if user has used all of their guesses
        if GUESSES_LEFT == 0:
            print('Sorry, game over.')
         # Continue if user still has guesses remaining
        else:
            GUESSES_LEFT = str(GUESSES_LEFT)
            print('You have ' + GUESSES_LEFT + ' guesses remaining, please try again.')
