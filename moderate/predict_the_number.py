

def mutate(ll):
    return [ (val + 1) % 3 for val in ll ]
    

def gen(n):    
    curr = []
    res = [0]
    for i in range(n):
        curr = mutate(res)
        print curr
        res += curr
    return res   



for i, val in enumerate(gen(10)):
    print "{}: {}".format(i, val)
    
print bin(25684)
# HOW!
print sum( [ d == '1' for d in bin(25684) ] ) % 3