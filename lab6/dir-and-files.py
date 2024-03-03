#EX1

import os

path = input()

print("Papka:")
for dir_name in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir_name)):
        print(dir_name)

print("\nFiles: ")
for file_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, file_name)):
        print(file_name)

#EX2

import os

path = input()

if os.path.exists(path):
    print("Path exists.")
else:
    print("Path does not exist!")

if os.access(path, os.R_OK):
    print("File is readable.")
else:
    print("File is not readable.")

if os.access(path, os.W_OK):
    print("File is writable.")
else:
    print("File is not writable.")

if os.access(path, os.X_OK):
    print("File is executable.")
else:
    print("File is not executable.")
    
#EX3

import os

path = input()
if os.path.exists(path):
    print("Basename: " + os.path.basename(path) + '\n' + "Dirname: " + os.path.dirname(path))
else:
    print("Path does not exist.")

#EX4

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
else:
    with open(file_path, 'r') as file:
        line_count = 0
        
        for line in file:
            line_count += 1
        
        print(f"Number of lines in {file_path}: {line_count}")


#EX5


my_list = ["apple", "banana", "orange", "kiwi"]

file_path = input("Enter a name for the file: ")

with open(file_path, "w") as file:
    for item in my_list:
        file.write(item + "\n")

print("List has been written to the file:", file_path)


#EX6
import os 
    
A = ord('A')
for i in range(A, A + 26):
    k = chr(i) + ".txt"
    file_name = os.path.join(os.getcwd(), k)
    with open(file_name, 'w') as file:
        file.write(file_name)
        
#EX7

import os

file_name = input("Enter the file name: ")

file_path = os.path.abspath(file_name)
if os.path.exists(file_path):
    print(f"{file_path} does not exist.")
    exit()

if os.access(file_path, os.W_OK):
    print(f"You do not have permission to delete {file_path}.")
    exit()
    
os.remove(file_path)
print(f"{file_path} has been deleted.")

#EX8

import os

file_path = input()

if not os.path.exists(file_path):
    print(f"{file_path} does not exist.")
    exit()

if not os.access(file_path, os.W_OK):
    print(f"You do not have permission to delete {file_path}.")
    exit()

os.remove(file_path)
print(f"{file_path} has been deleted.")