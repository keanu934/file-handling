import os

try:
    with open("garfields.txt") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")


# note: exceptions can be expensive

# A better option:

# check first to see if file exists
filename = "garfield.txt"
if os.path.exists(filename):
    with open(filename) as file:
        content = file.read()
        print(content)
else:
    print("File does not exist")
