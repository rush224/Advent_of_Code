import sys
import os

#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "1_1.txt"), "r") as cal_list:	
	temp = cal_list.read()		
	
#Changes source information from string to list by splitting with new line			
lines = temp.split("\n")

Cal_sum=[0]
tempsum = 0
Top_cals = 0

for count in lines:
    if count != '':
        x = int(count)
        tempsum += x
    else:
        Cal_sum.append(tempsum)
        tempsum = 0

i = 1
while i < 4:
    Top_cals += max(Cal_sum)
    Cal_sum.remove(max(Cal_sum))
    i+=1

print(Top_cals)
