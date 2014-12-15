import sys

digits = """-**----*--***--***---*---****--**--****--**---**--
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
*--*---*---**---**--****-***--***----*---**---***-
*--*---*--*-------*----*----*-*--*--*---*--*----*-
-**---***-****-***-----*-***---**---*----**---**--
--------------------------------------------------"""

table = {}
line1 = digits.split("\n")[0]
for i in range(10):
    start = 5 * i
    end = start + 5 
    
    for lineno, line in enumerate(digits.split("\n")):        
        if table.get(i) is None:
            table[i] = {}
        table[i][lineno] = line[start: end]
    


def print_digit(lines):    
    print lines[0]
    print lines[1]
    print lines[2]
    print lines[3]
    print lines[4]

def print_digits(liness):
    to_p = {0:"", 1:"", 2:"", 3:"", 4:"", 5:""}    
    for lines in liness:
        for lineno, line in lines.items():
            to_p[lineno] += line
    
    print to_p[0]
    print to_p[1]
    print to_p[2]
    print to_p[3]
    print to_p[4]
    print to_p[5]
    
def get_digit(digit):
    lines = {}
    for i in range(6):
        lines[i] = table[digit][i]
    return lines

def get_digits(digits):
    liness = []
    for digit in digits:
        if not digit.isdigit():
            continue
        liness.append(get_digit(int(digit)))
    return liness

with open(sys.argv[1]) as reader:
    for line in reader:
        print_digits(get_digits(line))