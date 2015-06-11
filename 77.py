def e_sieve(n):
    """ Returns  a list of primes < n, sorted by length and digit """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

# Probably massive overguess
limit = 10000000
primes = e_sieve(limit)

prime_summation_ways = {1: [], 2: [], 3: [], 4: [[2,2]], 5: [[3,2]], 6: [[2,2,2],[3,3]]}

i = 7
while True:
    primes_to_test = [prime for prime in primes if prime < i]
    print i
    summation_ways = []
    for prime_to_test in primes_to_test:
        if i-prime_to_test in primes_to_test:
            summation_ways.append(sorted([i-prime_to_test,prime_to_test]))
            # print "prime", i, i-prime_to_test
        for difference_way in prime_summation_ways[i-prime_to_test]:
            way = difference_way + [prime_to_test]
            way = sorted(way)
            # print "composite", i, i-prime_to_test, way
            summation_ways.append(way)
        # print i, summation_ways
        summation_ways = [list(x) for x in set(tuple(x) for x in summation_ways)]
        prime_summation_ways[i] = summation_ways
    if len(prime_summation_ways[i]) > 5000:
        for e, way in enumerate(prime_summation_ways[i]):
            print e, way
        print i, len(summation_ways)
        break
    else:
        print i, len(prime_summation_ways[i])
        # prime_summation_ways[i] = summation_ways
        i += 1
