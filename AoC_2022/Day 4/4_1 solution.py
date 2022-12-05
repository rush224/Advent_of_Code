import sys
import os
import string


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    temp = temp.read()
elves = temp.split("\n")
score = 0

for pair in elves:
    elf = pair.split(",")
    elf1 = elf[0].split("-")
    elf2 = elf[1].split("-")
    if ((int(elf1[1])>=int(elf2[1])) and (int(elf1[0])<=int(elf2[0]))) or ((int(elf1[1])<=int(elf2[1])) and (int(elf1[0])>=int(elf2[0]))):
        score += 1
    
print(score)