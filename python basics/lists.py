#Lists

fruits = ["Pear", "Pineapple", "Orange"] #Creates a list named "fruits" and appends "Pear" , "Pineapple" and "Orange" to the list.
print(fruits) #displays the list onto the screen: ['Pear' , 'Pineapple' , 'Orange']

#if we want to print a single item from the list, example "Pineapple" we use indexing
#fruit list item indexes
#"Pear" = 0 **first item has index 0
#"Pineapple" = 1
#"Orange" = 2

	#positive indexing
print(fruits[1]) #indexing starts with 0, so "Pear" has and index of 0 and "Pineapple" has an index of 1, etc.

	#negative indexing
print(fruits[-2]) #negative indexing starts from end of the list, in our case -1 refers to "Orange" and -2 refers to "Pineapple"


	#range of indexes
#we can specify range of indexes by specifying where to start and where to end the range
print(fruits[1:2]) # prints items(indexes) 1 to 2, so "Pineapple" and "Orange"

#Item values
fruits[1] = "Banana" 	#Changes the value of "Pineapple to "Banana"
print(fruits)

#If we want to lose the brackets, when printing our list we can use for-loop:
for x in fruits:
	print(x)			#prints our fruits without brackets, under each other.
	

	#If we have long lists and want to know how many items are in that list we can use len() method:
longlist = ["Email", "SSN", "Address", "Home Phone", "Mobile Phone", "DOB", "Date of Surgery"] #created a new list
print(len(longlist)) 	#will print the number of items in the specified list. In this case 7 items.

#if we want to add items to the list we can use append() method:
juices = [] #created a new empty list name "juices"
juices.append("orange_juice") #adds orange juice to the "juices" list
juices.append("apple_juice")
juices.append("cranberry_juice")
print(juices) #Prints the list juices onto the screen: ['orange_juice', 'apple_juice', 'cranberry_juice']

#if we want to remove items from the list we can use remove() method:
juices.remove("cranberry_juice") #removes cranberry_juice from the "juices" list.
print(juices)			#prints the list juices onto the screen: ['orange_juice', 'apple_juice']


#to delete lists, we use the del keyword
del juices #deletes juices list completely








