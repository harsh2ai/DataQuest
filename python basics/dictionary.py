# Dictionary (dict) that maps a fruit (Key) to its color (Value)
fruits_n_colors = {"Watermelon": "Green", "Apple": "Red", "Banana": "Yellow"}
print(fruits_n_colors)

# Shows how many pairs we have currently in fruits_n_colors
print(fruits_n_colors.__len__())

# New dict
new_fruits = {"Mango":"Orange", "Pineapple":"Orange"}

# Add new_fruits elements to fruits_n_colors
fruits_n_colors.update(new_fruits)
print(fruits_n_colors)
print(fruits_n_colors.__len__())

# It is possible to iterate over only the keys
for k in fruits_n_colors.keys():
    print("This is a key: " + k)

# It is possible to iterate over only the values
for v in fruits_n_colors.values():
    print("This is a value: " + v)

# It is possible to iterate over both keys and values
for i in fruits_n_colors.items():
    print("This is an item: %s, %s" % (i[0], i[1]))

# Creates a new dictionary with the same items
some_fruits = fruits_n_colors.copy()
print("This is the fruits_n_colors dict: %s" % fruits_n_colors)
print("This is the some_fruits dict: %s" % some_fruits)

# Changed Apple's value Red to Yellow-Red
some_fruits["Apple"] = "Yellow-Red"
print(some_fruits)

# Prints fruits_n_colors keys
print(fruits_n_colors.keys())

# Prints fruits_n_colors keys sorted
fruits_n_colors = sorted(fruits_n_colors)
print(fruits_n_colors)
