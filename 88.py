import numpy, sys, math, itertools

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

# factor p as a dictionary whose keys are factors and whose values are occurences thereof
# write an algorithm to generate combinations from this dictionary

# repeat for the range

all_combinations = dict()

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

primes = e_sieve(1000000)

def prime_factorization(n):
    """ Returns the prime factorization of n """
    index = 0
    factors = dict()
    while n > 1:
        prime = primes[index]
        if n % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            n /= prime
        else:
            index += 1
    return factors

def arrayify_factors_dict(dict):
    """ Returns an array from a dict of keys' occurences """
    array = list()
    for key, value in dict.items():
        for _ in range(value):
            array.append(key)
    return array

def count_total_factors(dict):
    """ Returns total occurences """
    total = 0
    for value in dict.values():
        total += value
    return total

def combinations_of_any_length(factors):
    """ Returns a list of combinations of s of any length.
    s is a dict whose keys are repeated their values' times
    """
    combinations = []
    total_factors = len(factors)
    for i in range(total_factors + 1):
        for c in list(itertools.combinations(factors, i)):
            remaining_factors = factors[:]
            for factor in list(c):
                if factor in remaining_factors:
                    remaining_factors.remove(factor)
            if len(remaining_factors) == 0:
                l = [list(c)]
                if l not in combinations: 
                    combinations.append(l)
            if len(remaining_factors) == 1:
                l = [list(c), remaining_factors]
                if l not in combinations: 
                    combinations.append(l)
            if len(remaining_factors) > 1 and len(remaining_factors) < len(factors):
                if all_combinations.has_key(numpy.prod(remaining_factors)):
                    remaining_combinations = all_combinations[numpy.prod(remaining_factors)]
                else:
                    remaining_combinations = combinations_of_any_length(remaining_factors)
                for remaining_factors_c in remaining_combinations:
                    l = [list(c)] + remaining_factors_c
                    l.sort()
                    if l not in combinations: 
                        combinations.append(l)
    all_combinations[numpy.prod(factors)] = combinations
    return combinations

def all_factorizations(n):
    """ Returns a unique list of ordered, non-trivial products
    of combinations of factors """
    p_factorization = prime_factorization(n)
    combinations = combinations_of_any_length(arrayify_factors_dict(p_factorization))
    factorizations = []
    for c in combinations:
        factorizations.append([numpy.prod(el) for el in c])
    return factorizations

def unique_product_sum(l):
    """ Returns the unique product sum from a list of n, n > 1 """
    return [1] * (numpy.prod(l) - numpy.sum(l)) + l

def all_product_sums(n):
    """ Returns all product sums of n's factors """
    product_sums = list()
    for f in all_factorizations(n):
        product_sums.append(unique_product_sum(f))
    return product_sums

def get_least_product_sums_to(k):
    least_product_sums = [0, 0, 4] + [None] * (k - 2)
    possible_p = 5
    while None in least_product_sums:
        possible_least_product_sums = all_product_sums(possible_p)
        for p in possible_least_product_sums:
            if len(p) <= k: 
                if least_product_sums[len(p)] is None:
                    least_product_sums[len(p)] = numpy.prod(p)
                    print "%s: %s" % (len(p), numpy.prod(p))
        possible_p += 1
        print "checking: %s" % possible_p
    return least_product_sums

least_product_sums = get_least_product_sums_to(12000)
unique_product_sums = list(set(least_product_sums))
unique_product_sums.sort()
print unique_product_sums
print numpy.sum(unique_product_sums)