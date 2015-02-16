import math
max_terms = 0
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
	# print primes
	return primes

def is_prime(n):
	if n > 1:
		for i in range(2,int(math.sqrt(n)+1)):
			if n%i==0:
				return False
	return True

def test_consecutive_primes_from(p_index):
	global solution
	global max_terms
	if max_terms*primes[p_index]<1000000:

		for i in range(1, len(primes)+1-p_index):
			s = sum(primes[p_index:i+p_index])
			if s in primes or is_prime(s) and s < 1000000:
				if i > max_terms:
					max_terms = i
					solution = s
					print max_terms, solution
	else:
		print max_terms, solution


primes = sieve(50000)

for e,p in enumerate(primes):
	test_consecutive_primes_from(e)
