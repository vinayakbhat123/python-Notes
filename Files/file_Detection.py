# File Detections

# Interview One-Liner
 # Writing files in Python is done using the open() function with write or append modes.

import os
file_path = "C:/Users/GURUPRASAD/Desktop/text.txt.txt"
if os.path.exists(file_path):
  print("File Found")
else:
  print("No File Found")

# Check only File Only File(Not Folder)
if os.path.isfile(file_path):
    print("It is a file")
elif os.path.isdir(file_path):
    print("That is directory")
else:
    print("File not found")

# check using (Pathlib)
from pathlib import Path
file = Path(file_path)
if file.exists():
    print("File exists")
else:
    print("File not found")


# using Try and Catch
try:
    with open(file_path, "r") as f:
        print("File exists")
        f.read()
except FileNotFoundError:
    print("File not found")




# Writing a file
# syntax
try:
    with open("data.txt", "r") as f:
        print("File exists")
except FileNotFoundError:
    print("File not found")

# File Writing Modes (Very Important ⭐)
# Mode	            Meaning
# "w"	          Write (creates / overwrites file)
# "a"	          Append (adds data, does not erase)
# "x"	          Create file, error if exists
# "w+"	        Write + read
# "a+"	        Append + read


#using Write a method
with open(file_path, "w") as f:
    f.write("Hello Python\n")
    f.write("File writing example")

# Append To a file
with open(file_path, "a") as f:
    f.write("\nThis is appended text")

# Writing multiple Lines
lines = ["Apple\n", "Banana\n", "Mango\n"]
with open(file_path, "w") as f:
    f.writelines(lines)

# writings numbers to a file
nums = [1, 2, 3, 4]

with open(file_path, "w") as f:
    for n in nums:
        f.write(str(n) + "\n")

# Example 6: Create File Safely (x mode)
try:
    with open(file_path, "x") as f:
        f.write("File created successfully")
except FileExistsError:
    print("File already exists")






## Reading Files 
# Reading files means opening a file and getting its content into your program.
# File Read Methods Summary
# Method                 	Use
# read()	                Read entire file
# readline()	            Read one line
# readlines()            	Read all lines
# for line in file	      Best practice

# syntax

# with open("file.txt", "r") as file:
#     data = file.read()


# Read Entire File
with open(file_path,"r") as f:
    print(f.read())

# Read Line By Line
with open(file_path, "r") as f:
    line = f.readline()
    print(line)

# Recommand for large files Loop throw a file
with open(file_path, "r") as f:
    for line in f:
        print(line.strip())
