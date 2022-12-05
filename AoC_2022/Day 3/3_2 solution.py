import sys
import os
import string


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
	ruck_list = temp.read()		
	
#Changes source information from string to list by splitting with new line			
rucks = ruck_list.split("\n")

top_sack = []
bottom_sack = []
num=list(range(1,53))
count = 0
alph=list(string.ascii_lowercase+string.ascii_uppercase)


scores = []

while count < len(rucks):           #looping through all of the rucksacks
    item = 0
    comps = 0
    abc = 0
    sack1 = rucks[count]
    sack2 = rucks[count+1]
    sack3 = rucks[count+2]
    for letter in alph:             #looping through alphabet for each item
        if letter in sack1:
            comps += 1
        if letter in sack2:
            comps += 1
        if letter in sack3:
            comps += 1   
        if comps == 3:
            scores.append(num[abc])
        abc += 1
        comps = 0
    count += 3
    
print(sum(scores))