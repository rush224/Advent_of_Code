import sys
import os

#Pulls source file from same location as executable and sets its to be a string 'r'
with open(os.path.join(sys.path[0], "input.txt"), "r") as r_data:	
	temp = r_data.read()	

comp=temp.split("\n")
score = []

for round in comp:
    if "X" in round:
        if "A" in round:
            score.append(3)
        elif "B" in round:
            score.append(1)
        else:
            score.append(2)
    elif "Y" in round:
        if "A" in round:
            score.append(4)
        elif "B" in round:
            score.append(5)
        else:
            score.append(6)
    else:
        if "A" in round:
            score.append(8)
        elif "B" in round:
            score.append(9)
        else:
            score.append(7)

print(sum(score))