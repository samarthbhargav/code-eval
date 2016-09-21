"""
URL: https://www.codeeval.com/open_challenges/153/

Date Started: 22-12-2014
Date Finished: 
    
Author: Samarth Bhargav
"""

import sys

def count_locked(n, m):
    locked = [False] * n
    
    for i in range(m - 1):
        #print "Before beat", locked
        for door in range(1, n, 2):
            locked[door] = True
        #print "After beat 1", locked
        for door in range(0, n, 3)[1:]:
            locked[door] = not locked[door]
        #print "After beat 2", locked

    locked[-1] = not locked[-1]
    
    return n - sum(locked) 
    
if len(sys.argv) == 2:
    with open(sys.argv[1]) as reader:
        for line in reader:
            m, n = map(int,line.strip().split())
            print count_locked(n, m)



### Test Cases
if __name__ == "__main__":
    assert count_locked(3, 1)  == 2
    assert count_locked(100, 100) == 50