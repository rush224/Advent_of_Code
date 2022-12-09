import sys
import os
import string


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    temp = temp.read()
raw=temp.split("\n")                    #splits into separate elements by new line

marker = []                             #Creating empty list to populate with marker
c1 = 0                                  #counter variable number 1
c2 = 0                                  #counter variable number 2

for element in raw:                     #separates raw data into individual elements
    signal = list(element)
    
for element in signal:                  #cycles through each element of the signal
    marker.append(element)              #adds individual elements to help search for marker
    if c1 >13:                          #starts looking for marker after list is four elements long
        del marker[0]                   #deletes first element in marker so marker is only four long
        print(marker)
        for char in marker:             
            count = marker.count(char)
            if count > c2:
                c2 = count
        if c2 == 1:
            break
    c1 += 1
    c2 = 0
    
print(c1+1)