infile = open("stuff/day2.dat")

numPad = [ 
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", "1", " ", " ", " "],
         [" ", " ", "2", "3", "4", " ", " "],
         [" ", "5", "6", "7", "8", "9", " "],
         [" ", " ", "A", "B", "C", " ", " "], 
         [" ", " ", " ", "D", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "]
         ]
        
curPos = [3, 1]
code = []

for line in infile:
    for char in line: 
        if char == "U" and numPad[curPos[0]-1][curPos[1]]!= " ":
            curPos[0] -= 1
        if char == "R" and numPad[curPos[0]][curPos[1] +1]!= " ":
            curPos[1] += 1
        if char == "L" and numPad[curPos[0]][curPos[1] -1]!= " ":
            curPos[1] -= 1
        if char == "D" and numPad[curPos[0] +1][curPos[1]]!= " ":
            curPos[0] +=1
        if char == '\n':
            code.append(numPad[curPos[0]][curPos[1]]) 
            break

print code

            
