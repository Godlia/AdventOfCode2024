import re
regexExp = "mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)"


def extract(string):
    tempArr = []
    if "don't()" in string:
        tempArr.append(False)
    elif "do()" in string:
        tempArr.append(True)
    else:
        #if mul( ) instruction
        string = str.replace(string, "mul(", "")
        string = str.replace(string, ")", "")
        for item in string.split(","):
            tempArr.append(int(item))
    
    # print(tempArr)
    return tempArr


with open("./Inputs/day3.txt") as file:
    ans = re.findall(regexExp, file.read())
    sum = 0
    run = True
    for item in ans:
        extracted = extract(item)
        if type(extracted[0]).__name__ == "bool":
            if extracted[0] == True:
                run = True
                print("Start adding")
            elif extracted[0] == False:
                run = False
                print("Skips")
        else:
            if run == True:
                print("Adding: ", extracted)
                sum += extracted[0] * extracted[1]
            else:
                print("Skipping: ", extracted)
    print(sum)