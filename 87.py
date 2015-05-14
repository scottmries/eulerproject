# The maximum prime we need to see is x**2 + x**3 + x**4 = 50000000
# only check to 50000000**0.5


def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

primes = e_sieve(int(50000000**(0.5)))

squares = [prime**2 for prime in primes]
cubes = [prime**3 for prime in primes if prime**3 < 50000000]
quads = [prime**4 for prime in primes if prime**4 < 50000000]

sums = set()

for square in squares:
    for cube in cubes:
        if cube + square < 50000000:
            for quad in quads:
                triple = sum([quad + cube + square])
                if triple < 50000000:
                    print triple
                    sums.add(triple)

print len(list(sums))
