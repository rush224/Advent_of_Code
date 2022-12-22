import sys
import os
import string
import math
import numpy as np


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    input = temp.read().split("\n")
    
i = 0                               #temporary counter
ii = 0
u = 0                               #horizontal distance for head to move
v = 0                               #vertical distance for head to move
knots = 10                          #number of points being tracked
Rope = np.zeros((knots,2))          #Coordinates of rope points (x,y)
T_pos = []                          #Contains coordinates that T has visited at least once
delta = 0                           #distance between head and tail
    
while i < len(input):                       #splits input into two lists, direction and distance
    dir=input[i].split(" ")[0]
    dist=int(input[i].split(" ")[1])
    if dir == "U":
        v = dist
        u = 0
    elif dir == "D":
        v = -dist
        u = 0
    elif dir == "L":
        u = -dist
        v = 0
    else:
        u = dist
        v = 0
    
    while u != 0 or v != 0:
        seg = 1    
                       
        while seg < knots:
            if seg == 1:
                if u != 0:
                    Rope[seg-1][0] = Rope[seg-1][0]+(u/abs(u))
                if v != 0:
                    Rope[seg-1][1] = Rope[seg-1][1]+ (v/abs(v))
              
            delta = math.sqrt((Rope[seg-1][0]-Rope[seg][0])**2 + (Rope[seg-1][1]-Rope[seg][1])**2)
            if delta == 2:                                  #moves segment if previous segment is two spaces vertical or horizontal
                if Rope[seg-1][0]-Rope[seg][0] == 2:
                    Rope[seg][0] = Rope[seg][0] + 1
                elif Rope[seg-1][0]-Rope[seg][0] == -2:
                    Rope[seg][0] = Rope[seg][0] - 1
                elif Rope[seg-1][1]-Rope[seg][1] == 2:
                    Rope[seg][1] = Rope[seg][1] + 1
                elif Rope[seg-1][1]-Rope[seg][1] == -2:
                    Rope[seg][1] = Rope[seg][1] - 1  
            elif delta > 2 and delta < 2.5:                                   #moves segment if previous segment is more than two spaces away 
                if Rope[seg-1][0]-Rope[seg][0] == 2:            #and located in different row and column
                    Rope[seg][0] = Rope[seg][0] + 1
                    Rope[seg][1] = Rope[seg-1][1]
                elif Rope[seg-1][0]-Rope[seg][0] == -2:
                    Rope[seg][0] = Rope[seg][0] - 1
                    Rope[seg][1] = Rope[seg-1][1]
                elif Rope[seg-1][1]-Rope[seg][1] == 2:
                    Rope[seg][1] = Rope[seg][1] + 1
                    Rope[seg][0] = Rope[seg-1][0]
                elif Rope[seg-1][1]-Rope[seg][1] == -2:
                    Rope[seg][1] = Rope[seg][1] - 1
                    Rope[seg][0] = Rope[seg-1][0]
            elif delta > 2.5:
                if Rope[seg-1][0]-Rope[seg][0] == 2 and Rope[seg-1][1]-Rope[seg][1] == 2:
                    Rope[seg][0] += 1
                    Rope[seg][1] += 1
                elif Rope[seg-1][0]-Rope[seg][0] == -2 and Rope[seg-1][1]-Rope[seg][1] == 2:
                    Rope[seg][0] -= 1
                    Rope[seg][1] += 1
                elif Rope[seg-1][0]-Rope[seg][0] == -2 and Rope[seg-1][1]-Rope[seg][1] == -2:
                    Rope[seg][0] -= 1
                    Rope[seg][1] -= 1
                elif Rope[seg-1][0]-Rope[seg][0] == 2 and Rope[seg-1][1]-Rope[seg][1] == -2:
                    Rope[seg][0] += 1
                    Rope[seg][1] -= 1
            if seg == (knots - 1) and list(Rope[seg]) not in T_pos:     #records position of tail if new
                T_pos.append([int(Rope[seg][0]),int(Rope[seg][1])])
                # print(Rope[seg], T_pos[-1])
            
            seg += 1
            
            # while ii < len(Rope):
                # temp = list(Rope)
                # print(list(temp[ii]), end = " ")
                # ii +=1
            # print(input[i], u, v)
            ii = 0
        if u != 0:
                u -= (u/abs(u))
        if v != 0:
            v -= (v/abs(v))
    i += 1
    
print(len(T_pos))
