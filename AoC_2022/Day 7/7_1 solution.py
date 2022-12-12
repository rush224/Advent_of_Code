import sys
import os
import string


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    temp = temp.read()

output=temp.split("\n")                     #splits into separate elements by new line
path = []                                   #list to track directory path
path_size = []
size = 0
DirectoryForDeletion = 70000000
c1 = 0

for lines in output:
    comms = lines.split(" ")
    
    if "$" in comms:
        if "cd" in comms[1]:
            if comms[2] !="..":
                path.append(comms[2])
                path_size.append(0)
            else:
                if path_size[-1] < DirectoryForDeletion and path_size[-1]>=1035571:
                    DirectoryForDeletion = path_size[-1]
                    print('success')
                del path[-1]
                del path_size[-1]

    
    if comms[0]!= "$" and comms[0].isnumeric():
        while c1 < len(path_size):
            path_size[c1] = path_size[c1]+int(comms[0])
            c1+=1
        c1 = 0
    print(path, path_size[-1])
    
print(DirectoryForDeletion)