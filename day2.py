def checkLevels(report):
    isDescending = None
    last = None
    for item in report:
        print("a")
        #if first element
        if last == None:
            last = item
            break
        #Guard clause
        if item == last:
            return False
        
        
        # strictly descending
        if item < last:
            isDescending = True
        
        #Strictly ascending
        if item > last:
            isDescending = False

        
        if abs(item - last) > 3:
            return False
        
        if item > last and isDescending:
            return False

        if item < last and not isDescending:
            return False
        
        last = item


    return True


with open("./Inputs/day2.txt") as file:
    numberOfSafeReports = 0
    for line in file:
        arr = line.split(" ")
        for count, item  in enumerate(arr):
            arr[int(count)] = int(item)
        print(arr)
        if checkLevels(arr):
            numberOfSafeReports += 1
    print(numberOfSafeReports)