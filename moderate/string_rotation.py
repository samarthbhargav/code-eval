"""
URL: https://www.codeeval.com/open_challenges/76/

Date Started: 20-12-2014
Date Finished: 20-12-2014
    
Author: Samarth Bhargav
"""

import sys

def rotate(string, start):
    return string[start:] + string[0:start]

def is_rotated(str1, str2):
    assert len(str1) > 0 and len(str2) > 0
    
    if len(str1) != len(str2):
        return False
    
    prevstart = 0
    while True:
        loc = str2.find(str1[0], prevstart)
        prevstart = loc + 1
        if loc == -1:
            return False        
        #print str1, rotate(str2, loc)
        if str1 == rotate(str2, loc):            
            return True
        
        

if len(sys.argv) == 2:
    with open(sys.argv[1]) as reader:
        for line in reader:
            f, s = line.split(",")            
            print is_rotated(f.strip(),s.strip())



### Test Cases
if __name__ == "__main__":
    assert not is_rotated("Basebont", "tBasefon")
    assert is_rotated("Hello", "oHell")    
    assert is_rotated("BBasefont", "tBBasefon")
    assert not is_rotated("BBasefont", "tBBcsefon")
    assert is_rotated("Hello", "lloHe")