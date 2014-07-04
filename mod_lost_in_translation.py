# -*- coding: utf-8 -*-
all_letters = map(chr, range(97,123))

encoded = """rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcp
tc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdrysi
de kr kd eoya kw aej icfkici re zjkr"""

plain = """the public is amazed by the quickness of the juggler
we think that our language is impossible to understand
so it is okay if you decided to quit"""

tr = {}

# create translation map
for e,p in zip(encoded, plain):
    if e in tr.keys() and tr[e] != p:
        print "AARRRGGGGG"
    tr[e]=p

# this i got from the challenge desc
tr['g'] = 'v'

# DUH! 
tr['h'] = 'x'

for let in all_letters:
    if let not in tr.keys():
        print let
        
def translate(encoded):
    decoded = ""
    for letter in encoded:
        decoded += tr[letter]
    return decoded
    

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print translate(test.strip())
test_cases.close()
