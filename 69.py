# brute forcing this will take forever.
# n/phi(n) will maximize as n increases and phi(n) decreases
# we therefore want as high as possible a number with as many factors as possible
# we want a _very_ composite number
# what's the product of the first some primes where that product <= 1000000?

import math

def primes_to(n):
	primes = [x for x in range(2,n+1)]
	for i in range(2,int(math.sqrt(n)+1)):
		for p in primes:
			if(i*p) in primes:
				primes.remove(i*p)
	return primes

primes = primes_to(1000)

product = 1
p = 0
while product <= 1000000:
	product *= primes[p]
	print product
	p += 1
print product
