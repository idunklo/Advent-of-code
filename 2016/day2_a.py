infile = open("stuff/day2.dat")

numPad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
curPos = [1, 1]
code = []

for line in infile:
    for char in line: 
        if char == "U" and curPos[0] != 0:
            curPos[0] -= 1
        if char == "R" and curPos[1] != 2:
            curPos[1] += 1
        if char == "L" and curPos[1] != 0:
            curPos[1] -= 1
        if char == "D" and curPos[0] != 2:
            curPos[0] +=1
        if char == '\n':
            code.append(numPad[curPos[0]][curPos[1]]) 
            break

print code

            
