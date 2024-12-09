def checkLevels(report):
    isDescending = None
    descendLock = False
    last = None
    isFirstIteration = True


    for i in range(len(report)):
        item = report[i]
        print(item)
        #if first element
        if isFirstIteration:
            last = item
            isFirstIteration = False
            continue
        #Guard clause
        if  item == last:
            return False
        
        # strictly descending
        if item < last and not descendLock:
            isDescending = True
            descendLock = True
        
        #Strictly ascending
        if item > last and not descendLock:
            isDescending = False
            descendLock = True

        
        if abs(item - last) > 3:
            return False
        
        if item > last and isDescending:
            return False

        if item < last and not isDescending:
            return False
        
        last = item
        isFirstIteration = False
    return True




with open("./Inputs/day2.txt") as file:
    numberOfSafeReports = 0
    for idx, line in enumerate(file):
        arr = line.split(" ")
        for count, item in enumerate(arr):
            arr[int(count)] = int(item)
        #print(arr) 
        if checkLevels(arr):
            print(idx , " - Safe : " , arr)
            numberOfSafeReports += 1
    print("safe: ", numberOfSafeReports)