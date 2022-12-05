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
    top_sack=rucks[count][: len(rucks[count]) // 2]
    bottom_sack=rucks[count][len(rucks[count]) // 2 :]
    #while item < len(top_sack):       #looping through the items in each sack
    abc = 0
    for letter in alph:             #looping through alphabet for each item
        if letter in top_sack:
            comps += 1
        if letter in bottom_sack:
            comps += 1
        if comps == 2:
            scores.append(num[abc])
        abc += 1
        comps = 0
        #item += 1
    count += 1
final_score = sum(scores)
print(final_score)