import sys
import os
import string
import math
import numpy as np


#Pulls source file from same location as executable and sets its to be a string 
with open(os.path.join(sys.path[0], "D1_input.txt"), "r") as temp:	
    input = temp.read().split("\n")
    
r_count = len(input)     #number of rows
c_count = 0             #number of columns
Alph = []               #Placeholder for alphabetic characters to be stored
Num = []                #Placeholder for numeric characters to be stored
Calibration = []        #Placeholder for summed values
Sum = 0                 #Placeholder for total calibration
Numbers = ["one","two","three","four","five","six","seven","eight","nine"]
i = 0                   #counter
ii = 0                  #secound counter

for x in input:
    # x.split("")
    Alph.append([])
    Num.append([])
    Calibration.append([])
    
    ii = 0    
    for y in x:
        if y.isnumeric() == False and ii >= 2:
            for nums in Numbers:
                if x.find(nums,0,ii+1)!= -1:
                    Num[i].append(str((Numbers.index(nums)+1)))
                    break
            if len(Num[i]) == 1:
                break
        elif y.isnumeric() == True:
            Num[i].append((y))
            break
        ii += 1
    
    ii = 0
    for y in x[::-1]:
        if y.isnumeric() == False and ii >= 2:
            for nums in Numbers:
                if x[::-1].find(nums[::-1],0,ii+1)!= -1:
                    Num[i].append(str((Numbers.index(nums)+1)))
                    break
            if len(Num[i]) == 2:
                break
        elif y.isnumeric() == True:
            Num[i].append((y))
            break
        ii += 1
    
    Calibration[i].append(int(Num[i][0] + Num[i][-1]))
    Sum += Calibration[i][0]
    i += 1
    
print(Sum)