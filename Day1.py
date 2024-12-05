from heapq import heapify, heappush, heappop

with open("./Inputs/Day1.txt") as file:
    leftHandMHeap = []
    rightHandMHeap = []
    
    for count, line in enumerate(file):
        string = line.split(",")
        leftHandMHeap.append(int(string[0]))
        rightHandMHeap.append(int(string[1]))
        
    heapify(leftHandMHeap)
    heapify(rightHandMHeap)
    
    distances = []
    
    for i in range(len(leftHandMHeap)):
        leftIx = heappop(leftHandMHeap)
        rightIx = heappop(rightHandMHeap)
        distance = abs(leftIx-rightIx)
        distances.append(distance)

    sum = 0
    
    for i in distances:
        sum += i
    
    print(sum)