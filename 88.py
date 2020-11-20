import numpy, sys, math

k = sys.argv[0] if len(sys.argv) > 0 else 12000

# for some set S in the naturals, s > 1,
# there is a unique productSum,
# viz. S U {1} * (prod(S) - sum(S))
# e.g.
# S = {4, 3}
# prod(S) = 12
# sum(S) = 7
# prodSum(S) = { 4, 3, 1, 1 ,1, 1, 1}

# proof: if any s changes, the sum may be preserved, but S is not
# if the number of ones changes, the product will be preserved, but the sum will not

# because the corresponding productSums of the combinations of factors of n are unique
# incrementing k, and filling the least productSum has yet to be filled,
# will solve this problem

# for some p, a potential least productSum, incrementing from 4
# what are its prime factors?
# what are the combinations of its prime factors?
# for each combination of prime factors,
# find the corresponding productSum
# if the productSum for some digit-length k for which p has a productSum is not yet known
# p is the least productSum for that k

# repeat for the range

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]