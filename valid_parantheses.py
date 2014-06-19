# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 14:42:07 2014

@author: hduser
"""

left = [ '{' , '[', '(']
right = [ '}', ']', ')' ]
def well_formed(string):
    stk = []
    
    for i in range(len(string)):
        if string[i]  in left:
            stk.append(string[i])
        else:
            sym = stk.pop()
            if left.index(sym) != right.index(string[i]):
                return False
    return True
