

choices = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]
curr = 0
flag = False
stops = [".", "!", "?"]

def choice():
    global curr
    ch = choices[curr % len(choices)]
    curr += 1
    return ch

import sys
    
with open(sys.argv[1]) as reader:
    for line in reader:        
        res = ""
        for letter in line:
            if letter in stops:                
                if flag:
                    res += choice()                
                else:
                    res += letter
                flag = not flag
            else:
                res += letter
                
        print res