import sys
import os
import string
import math
import numpy as np


#Pulls source file from same location as executable and sets its to be a string 
with open(os.path.join(sys.path[0], "D1P2_input.txt"), "r") as temp:	
    input = temp.read().split("\n")
    
r_count = len(input)     #number of rows
c_count = 0         #number of columns
Alph = []           #Placeholder for alphabetic characters to be stored
Num = []            #Placeholder for numeric characters to be stored
Calibration = []    #Placeholder for summed values
Sum = 0             #Placeholder for total calibration
i = 0               #counter

for x in input:
    # x.split("")
    Alph.append([])
    Num.append([])
    Calibration.append([])
    for y in x:
        if y.isnumeric() == False:
            Alph[i].append(y)
        elif y.isnumeric() == True:
            Num[i].append((y))
    
    Calibration[i].append(int(Num[i][0] + Num[i][len(Num[i])-1]))
    Sum += Calibration[i][0]
    i += 1