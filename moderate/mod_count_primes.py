
def sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True
        primes.append(i)

    return primes

def count_primes(primes, llimit, ulimit):
    count = 0
    for prime in primes:
        if prime >= llimit:
            if prime > ulimit:
                break
            count +=1
    return count


if __name__ =="__main__":
    import sys
    test_cases = open(sys.argv[1], 'r')
    nums = []
    m = 0
    for test in test_cases:
        if len(test) == 0:
            continue
        num = map(int, test.strip().split(','))
        if num[1] > m:
            m = num[1]
            
        nums.append(num)
    test_cases.close()
    
    primes = sieve(m)
    for num in nums:
        print count_primes(primes, num[0], num[1])
