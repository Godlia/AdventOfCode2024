import re


with open("./Inputs/day4.txt") as file:
    aa = file.read()
    print(len(aa))
    sum = 0
    for line in aa:
        sum += 1
        if line == "\n":
            print (sum)
            sum = 0