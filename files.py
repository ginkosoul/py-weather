import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

# try:
#     f = open("names.txt")
# except:
#     print("Error opening names.txt. File does not exist")
# finally:
#     f.close()
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)

# Append - creates the file if it doesn't exist

# f = open("names.txt", "a")
# f.write("\nNeil")
# f.write("\nDave")
# f.write("\nJohn")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# Create - creates the file if it doesn't exist

f = open("names.txt", "w")
f.write("\nI'm overwriting all of the content")
f.write("\nDave")
f.write("\nI'm the last")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Creates a file, but throws an exception if it exist

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()
else:
    print("Can't create dave.txt. Name conflict")

# Delete the file throws an exception if it doesn't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file doesn't exist")


# with open("names.txt") as f:
#     content = f.read()

# with open("dave.txt", "w") as f:
#     f.write(content)
