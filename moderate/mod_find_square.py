# -*- coding: utf-8 -*-

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pointstr = test.strip().split(", ")
    points = []
    for p in pointstr:
        p = p.replace(r'[()]', "")
        point = map(int, p.split(','))
        points.append(point)
    print points
test_cases.close()
