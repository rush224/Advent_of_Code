import sys
import os
import string
import math
import numpy as np


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    input = temp.read().split("\n")
    
i = 0               #temporary counter
ii = 0              #counter for unique positions
u = 0               #horizontal distance for head to move
v = 0               #vertical distance for head to move
H = [0,0]           #Coordinates of head (x,y)
T = [0,0]           #Coordinates of tail (x,y)
T_pos = []          #Contains coordinates that T has visited at least once
delta = 0           #distance between head and tail
    
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
        if u != 0:
            H[0] = H[0]+(u/abs(u))
        if v != 0:
            H[1] = H[1]+ (v/abs(v))
        delta = math.sqrt((H[0]-T[0])**2 + (H[1]-T[1])**2)
        if delta == 2:
            if abs(H[0]-T[0]) == 2:
                T[0] = T[0] + (u/abs(u))
            elif abs(H[1]-T[1]) == 2:
                T[1] = T[1] + (v/abs(v))
        if delta > 2:
            if abs(H[0]-T[0]) == 2:
                T[0] = T[0] + (u/abs(u))
                T[1] = H[1]
            elif abs(H[1]-T[1]) == 2:
                T[1] = T[1] + (v/abs(v))
                T[0] = H[0]
        if T not in T_pos:
            T_pos.append([T[0],T[1]])
        # print(T, T_pos[-1])

        if u != 0:
            u -= (u/abs(u))
        if v != 0:
            v -= (v/abs(v))
    i += 1
    
