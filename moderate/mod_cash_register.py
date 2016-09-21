# -*- coding: utf-8 -*-
from collections import OrderedDict

change = [('PENNY', .01),
('NICKEL', .05),
('DIME', .10),
('QUARTER', .25),
('HALF DOLLAR', .50),
('ONE', 1.00),
('TWO', 2.00),
('FIVE', 5.00),
('TEN', 10.00),
('TWENTY', 20.00),
('FIFTY', 50.00),
('ONE HUNDRED', 100.00)
]

change = OrderedDict(change[::-1])

def get_largest(m):
    for name, val in change.items():
        if val <= m:
            return name, val

def get_change_list(paid, cost):
    
    if paid > cost:
        return ["ERROR"]
    elif paid == cost:
        return ["ZERO"]
    ret = []
    diff = cost - paid
    while diff != 0.0:
        if diff < 0.01:
            break
        key,val = get_largest(diff)
        ret.append(key)
        diff -= val
    return ret
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    paid, cost = map(float, test.strip().split(';'))
    print ",".join(get_change_list(paid, cost))

test_cases.close()
