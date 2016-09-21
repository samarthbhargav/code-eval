"""
URL: https://www.codeeval.com/open_challenges/5/

Date Started: 20-12-2014
Date Finished: 
    
Author: Samarth Bhargav
"""

import sys

def detect_cycles(sequence):
    assert sequence is not None and len(sequence) > 0
    hare = 0
    tortoise = 0
    n = len(sequence)
    while True:        
        if not hare < n:
            return []
        hare += 1
        if not hare < n:
            return []
        hare += 1
            
        tortoise += 1
        
        print sequence[tortoise]
        print sequence[hare]
        print
        if sequence[hare] == sequence[tortoise]:
            return sequence[tortoise: hare]
        
    
    return None



if len(sys.argv) == 2:
    with open(sys.argv[1]) as reader:
        for line in reader:
            print " ".join(detect_cycles(line.split()))



### Test Cases
if __name__ == "__main__":
    assert detect_cycles("3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49".split()) == ["49"]