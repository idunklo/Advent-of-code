import numpy as np

directions = np.genfromtxt("stuff/day1.dat", dtype = 'str', delimiter = ', ')

myPos = [0, 0]
myDir = [0, 1] 

rot = [[ 0, 1],
       [-1, 0]]  

R = [myPos]  
S = []

for direction in directions:
    if direction[0] == "R":
        myDir = np.dot(rot, myDir)
    else:
        myDir = - np.dot(rot, myDir)

    for blocks in range(1, int(direction[1:])+1):
        curPos = (myPos + myDir*blocks).tolist()

        for prePos in R: 
            if curPos == prePos:
                S.append(prePos)   
                
        R.append(curPos)

    myPos += myDir * int(direction[1:])

print abs(S[0][0]) + abs(S[0][1])
#print abs(myPos[0]) + abs( myPos[1])


