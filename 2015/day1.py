infile = open("input/day1.dat")

floor = 0  
pos = 0

for line in infile:
    for par in line:
        pos +=1

        if par == "(":
            floor += 1
        elif par == ")":
            floor -= 1

        if floor == -1:
            print pos


print floor


