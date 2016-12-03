import numpy as np

infile = open("stuff/day3.dat")

counter = 0   
tmp = 0
a = np.zeros([3,3])


for line in infile: 
    a[tmp, :] = np.array([int(x) for x in line.split()])
    
    if tmp == 2:
        for i in range(3):
            if max(a[:, i]) < a[a[:,i].tolist().index(max(a[:, i])) -1, i] + a[a[:, i].tolist().index(max(a[:, i])) -2, i]:
                counter += 1

        tmp = 0
        a = np.zeros([3,3])

    else:
        tmp += 1

print counter

