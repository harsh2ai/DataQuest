"""
Examples of basic regex patterns for working with a phone number.
"""
import re

sample_phone_number = "+1-234-567-8901"
number_with_spaces = "1 234 567 8901"
number_all_hyphens = "1-234-567-8901"
phone_numbers = [sample_phone_number, number_with_spaces, number_all_hyphens]

print(
    """
we can use regex to match groups of digits, regardless of
what separates them. \D matches non digits, so we skip
characters like '+'. [\D]* matches zero or more non-digits
\d matches digits, \d+ matches one or more digits.
'.' matches any single character. The
parentheses split the result up into four groups
re.match returns our matching groups.
-----------------------------------------------------------
"""
)


for phone_number in phone_numbers:
    matches = re.match(r"[\D]*(\d+).(\d+).(\d+).(\d+)", phone_number)
    print(f"country code:      {matches.group(1)}")
    print(f"area code:         {matches.group(2)}")
    print(f"first digit group: {matches.group(3)}")
    print(f"next digit group:  {matches.group(4)}")
    print("--------------------------------------")
