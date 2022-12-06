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
c3 = 0      #stand in variable 3
stacks = []
content = []

for line in orders:                     #identifies last line of box diagram
    if "1" in line:
        i = int(line[-2])               #i is number of stacks
        while c1<i:                    
            stacks.append(c1+1)         #creates list with number of stacks 
            content.append([])          #creates list with empty nested lists for stack contents
            c1 += 1
        c1 = 0
        break
    c2 += 1                             #c2 is row of numbers


for c1 in stacks:                       #c1 is number of working stack 
    index = orders[c2].find(str(c1))    #locates index of desired stack    
    count = 0
    while count < c2:                      #starts at top of orders and extracts box ID
        c3 = orders[count][index]
        if c3 != " ":
            content[c1-1].append(c3)
        count += 1
    print(content[c1-1])

# c1 = 0

# for row in orders:
    # if row != "/n":
        # del orders[c1]
    # else:
        # del orders[row]
        # break
    # c1 += 0