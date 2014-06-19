# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 18:03:32 2014

@author: hduser
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if len(test.strip()) == 0:
        continue
    test = test.strip().split(';')
    string = test[0]
    subs = test[1].split(',')
    for i in range(len(subs) - 1):
        string = string.replace(subs[i],subs[i+1], 1)
        print string
        i+=1
    
test_cases.close()
