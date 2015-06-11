
import itertools


def e_sieve(n):
    """ Returns  a list of primes < n, sorted by length and digit """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    primes_of_length = dict()
    for i in range(1, len(str(n))):
        primes_of_length[i] = [[]]*10
        for j in range(1, 10):
            primes_of_length[i][j] = list()
    for prime in [2] + [i for i in xrange(3, n, 2) if sieve[i]]:
        primes_of_length[len(str(prime))][int(str(prime)[0])].append(prime)
    return primes_of_length

# This limit accounts for all 4-digit pairs, which we assume the solution will not exceed
limit = 100000000
primes_of_length = e_sieve(limit)
# The size of a set of pairables that a prime must have to qualify
set_length = 4
# key: a prime, value: a list of primes that pair with it
pairs_with = dict()

for i in range(1,9):
    if i in primes_of_length:
        if len(primes_of_length[i]) > 0:
            for j in range(1,10):
                for prime in primes_of_length[i][j]:
                    for digit_index in range(len(str(prime))):
                        if digit_index > 0 and digit_index < len(str(prime)):
                            if int(str(prime)[digit_index]) != 0:
                                left = int(str(prime)[:digit_index])
                                right = int(str(prime)[digit_index:])
                                # Don't bother with primes longer than half the limit, and only check primes less than or equal to left
                                if len(str(left)) < (len(str(limit)))/2.0 and left >= right:
                                    print left, right
                                    # Check that left, right and concated right and left are prime
                                    if left in primes_of_length[len(str(left))][int(str(left)[0])] and right in primes_of_length[len(str(right))][int(str(right)[0])] and int(str(right) + str(left)) in primes_of_length[len(str(int(str(right) + str(left))))][int(str(int(str(right) + str(left)))[0])]:
                                        # Add them to the dict
                                        pairs_with.setdefault(left,[]).append(right)
                                        pairs_with[left] = sorted(list(set(sorted(pairs_with[left]))))

sets_of_5 = dict()

for key, value in pairs_with.items():
    if len(value) > set_length - 1:
        # Get all possible sets of pairables of the current prime of length set_length
        test_sets = list(itertools.combinations(value,set_length))
        for test_set in test_sets:
            test_set = [key] + [t for t in test_set]
            print test_set
            # Get all possible pairs of the set
            test_pairs = list(itertools.combinations(test_set,2))
            print test_pairs
            # If the all of the higher of the test_pair values has pairables and all of the the lower values are one of them
            if all([max(test_pair[0],test_pair[1]) in pairs_with and min(test_pair[0],test_pair[1]) in pairs_with[max(test_pair[0],test_pair[1])] for test_pair in test_pairs]):
                print test_set, sum(test_set)
                # add them to the solution set
                sets_of_5[sum(test_set)] = test_set

# Print the solution and its sum
print sets_of_5[min(sets_of_5.keys())], min(sets_of_5.keys())
