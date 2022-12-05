import sys
import os
import string


#Pulls source file from same location as executable and sets its to be a string
with open(os.path.join(sys.path[0], "input.txt"), "r") as temp:	
    temp = temp.read()
elves = temp.split("\n")                #splits input file into separate elements by detecting new lines
score = 0

for pair in elves:
    elf = pair.split(",")               #splits each elf pair by detecting the comma
    elf1 = elf[0].split("-")            #creates a list that defines the bounds of elf1's border by splitting at the hyphen. repeats for elf2
    elf2 = elf[1].split("-")
    if ((int(elf2[0])>=int(elf1[0]))and(int(elf2[0])<=int(elf1[1]))) or ((int(elf1[0])>=int(elf2[0]))and(int(elf1[0])<=int(elf2[1]))):
        score += 1
print(score)