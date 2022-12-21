import sys
import os
import string
import numpy as np


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    forest = temp.read().split("\n")

i = 0
score = 0
rotations = 0
v_len = len(forest)
h_len = len(forest[0])
T_score = []
v_pos = 1


while i < len(forest):
    forest[i] = list(map(int,forest[i]))
    if i ==0:
        grid = np.array(forest[0])
    else:
        grid= np.vstack((grid,forest[i]))
    i+=1

rgrid = np.rot90(grid,3)


while v_pos < (v_len-1):                #loops through each row of tree
    h_pos = 1
    
    while h_pos < (h_len-1):            #loops through each tree in row
        i = 1
        L_count = 0
        L_height = 0
        R_count = 0
        R_height = 0
        U_count = 0
        U_height = 0
        D_count = 0
        D_height = 0
        tree = grid[v_pos][h_pos]
        L_view = np.flip(grid[v_pos][: h_pos])
        R_view = grid[v_pos][h_pos+1 :]
        U_view = np.flip(grid[:,h_pos][: v_pos])
        D_view = grid[:,h_pos][v_pos+1 :]
        
        for view in L_view:
            L_count += 1
            if view >= tree:
                break
        for view in R_view:
            R_count += 1
            if view >= tree:
                break
        for view in U_view:
            U_count += 1
            if view >= tree:
                break
        for view in D_view:
            D_count += 1
            if view >= tree:
                break
                
        # if L_count*R_count*D_count*U_count > 1000:        
            # print(tree)
            # print(L_count, L_view)
            # print(R_count, R_view)
            # print(D_count, D_view)
            # print(U_count, U_view)
            # input()
        T_score.append(L_count*R_count*D_count*U_count)
                # print(tree, v_pos, h_pos, T_Score)
        
        h_pos += 1
        
    v_pos += 1
    
