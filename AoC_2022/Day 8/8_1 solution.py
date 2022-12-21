import sys
import os
import string
import numpy as np


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    forest = temp.read().split("\n")

i = 0
count = 0
rotations = 0
v_len = len(forest)
h_len = len(forest[0])
v_pos = 0

while i < len(forest):
    forest[i] = list(map(int,forest[i]))
    if i ==0:
        grid = np.array(forest[0])
    else:
        grid= np.vstack((grid,forest[i]))
    i+=1

rgrid = np.rot90(grid,3)


while v_pos < (v_len):                #loops through each row of tree
    h_pos = 0
    rh_pos = v_len
    while h_pos < (h_len):            #loops through each tree in row
        tree = grid[v_pos][h_pos]
        if v_pos == 0 or v_pos == (v_len-1) or h_pos == 0 or h_pos == (h_len-1):                #automatically counts trees on border
            count+=1
            # print("1", v_pos, h_pos, count)
        elif (h_pos == 1 and tree>grid[v_pos][0]) or (h_pos == h_len-2 and tree>grid[v_pos][v_len-1]):  #counts second tree if greater than border tree
            count += 1
            print("2", v_pos, h_pos, count)
        elif h_pos!=1 and tree>max(grid[v_pos][:(h_pos)]):      #counts tree if greater than all trees to left                        
            count+=1
            print("4", v_pos, h_pos, count)
        elif h_pos!=(h_len-2) and tree > max(grid[v_pos][(h_pos+1):]):    #counts tree if greater than all trees to right
            count+=1
            print("5", v_pos, h_pos, count)
        elif (v_pos == 1 and tree>grid[:,h_pos][0]) or (v_pos == v_len-2 and tree > grid[:,h_pos][v_len-1]): #counts second tree in column if greater than border tree
            count+=1
            print("6", v_pos, h_pos, count)
        elif (v_pos != 1 and tree>max(grid[:,h_pos][: v_pos])) or (v_pos != v_len-2 and tree>max(grid[:,h_pos][v_pos+1 :])):
            count +=1
            print("7", v_pos, h_pos, count)
            
        h_pos += 1
    v_pos += 1
    
print(count)