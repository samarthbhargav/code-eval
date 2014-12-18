import sys

def un_repeat(line):
    prev_letter = line[0]
    res = prev_letter
    for letter in line[1:]:
        if letter == prev_letter:
            continue
        
        res += letter
        prev_letter = letter
    return res
    
with open(sys.argv[1]) as reader:
    for line in reader:
        print un_repeat(line)