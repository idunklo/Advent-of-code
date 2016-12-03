infile = open("stuff/day3.dat")  

counter = 0

for line in infile:
    a = [int(x) for x in line.split()]   

    if max(a) < a[a.index(max(a))-1] + a[a.index(max(a))-2]:
        counter += 1

print counter



