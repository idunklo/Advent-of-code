import hashlib

puzzleInput = "abbhdwsy"  

def hexa_finder(start_int, num_zeros):
    hexa_hash = hashlib.md5(puzzleInput).hexdigest()
    integer = start_int

    while hexa_hash[0:len(num_zeros)] != num_zeros:
        integer += 1
        hexa_hash = hashlib.md5(puzzleInput + str(integer)).hexdigest()
    print hexa_hash  
    return integer

new_int = 0

for i in range(30):
    new_int = hexa_finder(i + new_int, "00000") 






