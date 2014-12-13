def juggle_zeroes(line):
    zeroes = line.split()    
    it = iter(zeroes)
    binstr = ""
    for z in it:
        z2 = next(it)
        if z == "0":
            binstr += z2
        else:
            binstr += "1" * len(z2)
    return int(binstr, 2)
        


import sys
with open(sys.argv[1]) as reader:
    for line in reader:
        print juggle_zeroes(line)