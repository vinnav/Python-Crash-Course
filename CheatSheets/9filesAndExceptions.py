# READ FILES
with open("file.txt") as file_object:# Opena a file and close it when not needed
    contents = file_object.read()    # Read from a file and assign its content
print(contents)                      # Print its content

with open("files//file.txt") as file_object # Open file with relative path

file_path = "/home/other/files/file.txt"    # Open file with absolute path
with open(file_path) as file_object             

# Reading line by line
with open("file.txt") as file_object:
    for line in file_object:
        print(line)

# Store file lines in a list
with open("file.txt") as file_object:# Even if the file closes after the "with"
    lines = file_object.readlines()  # block, you can keep working with the list
for line in lines:
    print(line.rstrip())             # Remove spaces and new lines at the end

for line in lines:
    text =+ line.strip()             # Put all the content in a String

# WRITE FILES
filename = "filename.txt"
with open(filename, "w") as file_object: # Args: 1 file name, 
                                         #       2 open mode
                                         #          "w" = write
                                         #          "r" = read
                                         #          "a" = append
    file_object.write("Write text") # Write in the file

# Append mode
with open(filename, "a") as file_object: # Append mode doesn't overwrite
    file_object.write("Text appended") 

# Count words
words = file.split()
numWords = len(words)

# EXCEPTIONS

try:                                    # Try to run the code
    print(5/0)
except ZeroDivisionError:               # Run if exception is raised
    print("You can't divide by 0!")
else:                                   # Run if tried code succeded
    print("Division success")

except FileNotFoundError:               # File not found
    pass                                # Fails silently

# STORING DATA
import json
data = [2, 3, 5, 7, 11, 13]
filename = "file.json"
with open(filename, "w") as f:
    json.dump(data, f)              # Stores data into file.json

with open(filename) as f:
    numbers = json.load(f)          # Retrieve the stored data

Pag 208, ex 10-12


