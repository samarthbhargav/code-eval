def rev_list_k(my_list, k):
    def rev(li):
        return li[::-1]
    l = []
    for i in range(0,len(my_list), k):
        if k+i > len(my_list):
            l.extend((my_list[i:]))
        else:
            l.extend(rev(my_list[i:k+i]))
    return map(str,l)
        
        
    
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    my_list, k = test.strip().split(';')
    my_list = map(int, my_list.split(','))
    print ",".join(rev_list_k(my_list, int(k)))
    
test_cases.close()
