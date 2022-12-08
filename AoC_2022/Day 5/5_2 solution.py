import sys
import os
import string


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    temp = temp.read()
orders=temp.split("\n")                 #splits into separate elements by new line
log = 0
c1 = 0      #stand in variable 1
c2 = 0      #stand in variable 2       
numr = 0    #variable to hold row index of stack numbers            
stacks = []
content = []
dirs = []

for line in orders:                     #identifies last line of box diagram
    if "1" in line:
        i = int(line[-2])               #i is number of stacks
        while c1<i:                    
            stacks.append(c1+1)         #creates list with number of stacks 
            content.append([])          #creates list with empty nested lists for stack contents
            c1 += 1
        c1 = 0
        break
    numr += 1                             #numr is row of numbers

L2 = orders[numr+1]

for c1 in stacks:                       #c1 is number of working stack 
    index = orders[numr].find(str(c1))    #locates index of desired stack    
    count = 0
    while count < numr:                      #starts at top of orders and extracts box ID
        c2 = orders[count][index]
        if c2 != " ":
            content[c1-1].append(c2)
        count += 1
    #print(content[c1-1])               #prints out current stacks in a rotated list format

for rows in content:
    index = content.index(rows)
    content[index].reverse()

c1 = 0
c2 = 0

while c1 <= numr+1:                       #deleting orders content excepting move directions
    del orders[0]
    c1 += 1

c1 = 0

for rows in orders:
    c2 = 0
    dirs = orders[c1].split(" ")
    for element in dirs:
        if element.isdigit:
                i = dirs.index(str(element))
                dirs.pop(i)
    dirs = list(map(int,dirs))
    while c2 < dirs[0]:                                                     #copies boxes from origin stack to destination
        content[dirs[2]-1].append(content[dirs[1]-1][-(dirs[0]-c2)])        #dirs[0] is number of boxes // dirs[1] is origin stack // dirs[2] is destination stack
        c2 += 1 
    c2 = 0
    while c2<dirs[0]:                                                       #removes boxes from origin stack
        content[dirs[1]-1].remove(content[dirs[1]-1][-1])
        c2 += 1
    c1 += 1


    
# for row in content:
    # print(row[-1])