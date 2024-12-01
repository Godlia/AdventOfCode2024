from heapq import heapify, heappush, heappop

with open("day1.txt") as file:
    leftHandMHeap = []
    rightHandMHeap = []
    
    
    
    for count, line in enumerate(file):
        string = line.split(",")
        leftHandMHeap.append((int(string[0]), count))
        rightHandMHeap.append((int(string[1]), count))
        
    heapify(leftHandMHeap)
    heapify(rightHandMHeap)
    
    distances = []
    
    for item in leftHandMHeap:
        leftIx = heappop(leftHandMHeap)[1]
        rightIx = heappop(rightHandMHeap)[1]
        distance = abs(leftIx-rightIx)
        distances.append(distance)

    sum = 0
    
    for i in distances:
        sum += i
    
    print(sum , distances)
