print("\nPrinting one line at a time:")

# Opens the file in read mode and prints each line in the file.
# Automatically close the file when done (this is done using
# the width statement
with open("test_file.txt", "r") as file:
    for line in file:
        # Prints each line in the file with the new line characters stripped
        print(line.strip("\n"))

# Opens the file in read mode and prints contents of the file and auto closes it
print("\nPrinting the contents of the file:")
with open("test_file.txt", "r") as file:
    file_contents = file.read()
    print(file_contents)

# Opens the file in read mode and reads a single line from the file and auto closes it
print("\nReading a single line from the file")
with open("test_file.txt", "r") as file:
    line = file.readline()
    print(line)

# Opens the file in append mode and writes a line to the file and auto closes it
print("\nAppending a line to end of file")
with open("test_file.txt", "a") as file:
    file.write("\nadded line")

# Opens the file in write mode to overwrite a file and auto closes it
print("\nOverwriting contents in file")
with open("overwrite_file.txt", "w") as file:
    file.write("overwriting file")

# Opens a new file in write mode and writes content to it
print("\nCreating a new file with content")
with open("new_file.txt", "w") as file:
    file.write("created new file")
