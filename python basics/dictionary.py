thisdict = {   #create a dictionary with initial infomration
  "Name": "Fabio",
  "Age": "20",
  "Location": "Colombia"
}
## "Name", "Age", "Location" are the keys and 
## "Fabio", "20" and "Colombia" are the informtion stored
print(thisdict)

thisdict["City"] = "Barranquilla" #insert another key with its information
print(thisdict)
thisdict["City"] = "Cartagena" #change information with a specific key
print(thisdict)

#iterate through dictionary
for elem in thisdict: #for each key in the dictionary
  print(elem) 

sz= len(thisdict) # store the size of the dictionary
print(sz)   #print the size of the dictionary

thisdict.pop("City") # remove the element and the key with value "City" from the dictionary
print(thisdict)

dict2 = thisdict.copy() # copy all the elements and values from thisdict and store a copy in dict2
dict2["sex"] = "M" 
print(dict2) 
print(thisdict)
