# # How many pairs of mutually prime numbers n,d are there for n,d <= 1000000 where n,d have no common factor but 1?
# # Make this more efficient
# Picture a grid 1,000,000 x 1,000,000
# Slice it in half into a triangle
# Include all values in row 1
# Include all odd values in row 2
# Include all odd, non-3-divisible values in row 6

# For each row, get that row's improper factors (including the row number itself)
# For each factor, iterate through it, eliminating anything divisible by it

# Basically a 2-D Sieve of Erastothenes

# No. For each prime row, generate a list of fractions that are not reduced.
# Do this for the given row, and for all rows that are multiples of the prime row.
# For 2, the list would include (2*k,2*j) k < j; k,j < 1000000/2
# For 3, the list would include (3*k,3*j) k < j; k,j < 1000000/3, where k,j !| 2 (do not divide 2)
# These need not be listed, only counted
# Then figure out the total number of possible (n,d) pairs and subtract

# No again. Use Euler's product formula, which gives phi(n) as n sigma (1-1/p) for p|n
# for the primes up to sqrt(1000000), just make a list for each integer of its factors as you progress up the primes

import math

factor_list = dict()

solution = 0

def sieve(n):
	primes = list()
	for i in range(2,n+1):
		primes.append(i)
	p = 0
	while p < len(primes):
		for r in primes[p+1:]:
			if r%primes[p]==0:
				primes.remove(r)
		p+=1
	if int(p%(n/10.0))==0:
		print p
	return primes

# More efficient sieve; what's going on here?

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = e_sieve(1000000)
# primes = sieve(100000)
# primes = sieve(7)

print primes

for p in primes:
	# for k in range(1,8/p+1):
	for k in range(1,1000000/p+1):
		# print "p,k %s,%s \n" % (p,k)
		if p*k in factor_list:
			factor_list[p*k].append(p)
		else:
			factor_list[p*k] = [p]


for k in factor_list:
	product = k
	for f in factor_list[k]:
		product*= (1.0-1.0/f)
	solution += product

print int(solution)
