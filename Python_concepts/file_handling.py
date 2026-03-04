# To store data permanently, even after the program ends.
# To access external files like .txt, .csv, .json, etc.
# To process large files efficiently without using much memory.
# To automate tasks like reading configs or saving outputs.

f = open("geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

#Reading a File in Read Mode (r)
file = open("geek.txt", "r")
content = file.read()
print(content)
file.close()

#Writing to a file (overwrites if file exists)
with open("geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

#closing file
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()