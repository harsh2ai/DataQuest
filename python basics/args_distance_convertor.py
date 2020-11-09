'''In this example we show how Python can take arguments from the command line
to use as variables within a program.
This program will take in a distance and unit of measurement and then display it
in different units of measurements.
Usage of this program will be as follows (Python 3.x):
python args_distance_convertor.py --distance (some distance value) --unit (some unit value:
metre,km, yard, mile)
or
python args_distance_convertor.py -d (some distance value) -u (some unit value:
metre,km, yard, mile)

example: python args_distance_convertor.py -d 1 -u mile
'''

# import argparse module
import argparse

# initiate the PARSER
PARSER = argparse.ArgumentParser()

# Choose some arguments that we will accept and set these up
# Accept the switch -d or --distance for distance and ensure this value is of type "float"
PARSER.add_argument("--distance", "-d", type=float, help="Please provide a numeric value for the distance that you would like to convert.")
# Accept the switch -u or --unit for unit of measurement and check that this is of type "string"
# Use argparse's 'choice' option to limit possible values to specific measurement units and typecase
PARSER.add_argument("--unit", "-u", type=str, choices=['metre', 'km', 'yard', 'mile'], help="Please provide the unit for the distance that you would like to convert.")

# read arguments from the command line
ARGS = PARSER.parse_args()

# These values are now avaulable as the variables args.distance and args.unit

# Convert distance to a standard unit of metres to make further calculations easier
if ARGS.unit == "metre":
    METRES = ARGS.distance
if ARGS.unit == "km":
    METRES = ARGS.distance*1000
if ARGS.unit == "yard":
    METRES = ARGS.distance*0.9144
if ARGS.unit == "mile":
    METRES = ARGS.distance*1609.34

# Do the maths to work out the distance conversions
# Use the round function to round to 2 decimal places
# The round function takes two values, the first value is the value to round
# the secod value is the number of decimal places to round to.

KMS = round(METRES/1000, 2)
YARDS = round(METRES*1.09361, 2)
MILES = round(METRES*0.000621371, 2)

print('//////////////////////////////////////////////////////')
print('Here are the distance conversions based on your input: ')
print('//////////////////////////////////////////////////////')

# Insert blank line
print()

# For each line below we use the format method of the print command to insert
# the value of the variable in between the {}
print('{} metres'.format(METRES))
print('{} kilometers'.format(KMS))
print('{} yards'.format(YARDS))
print('{} miles'.format(MILES))
