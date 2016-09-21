# -*- coding: utf-8 -*-

def conv_to_regexp(binstr):
    regex = ""
    for char in binstr:
        if char == "0":
            regex += "A+"
        else:
            regex += "((A)+|(B)+)" 
    return regex
    

import sys
import re
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    binstr, string = test.strip().split()
    regex = conv_to_regexp(binstr)
    
    if len(re.findall(regex, string )) != 0:
        print "Yes"
    else:
        print "No"
    

test_cases.close()

