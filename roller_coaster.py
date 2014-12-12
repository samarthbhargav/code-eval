def roller_coaster(line):
    upper = True
    res = ""
    for ch in line:
        if ch.isalpha():
            if upper:
                res += ch.upper()
                upper = False
                continue
            else:
                res += ch.lower()
                upper = True
                continue
        res += ch
    return res
            
            

import sys
with open(sys.argv[1]) as reader:
    for line in reader:
        print roller_coaster(line)