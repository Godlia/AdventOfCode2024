import re
regexExp = 'mul\([0-9]{1,3},[0-9]{1,3}\)'

def extract(string):
    string = str.replace(string, "mul(", "")
    string = str.replace(string, ")", "")
    
    tempArr = []
    for item in string.split(","):
        tempArr.append(int(item))
    
    
    return tempArr


with open("./Inputs/day3.txt") as file:
    ans = re.findall(regexExp, file.read())
    sum = 0
    for item in ans:
        ya = extract(item)
        sum += ya[0] * ya[1]
    print(sum)