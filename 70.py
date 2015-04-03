# phi(n) must be smaller than n but have the same number of digits as n, so only those permutations should be considered
# # 

from operator import mul
import itertools

def sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return ([2] + [i for i in xrange(3,n,2) if sieve[i]],[i for i in xrange(3,n,2) if not sieve[i]])

def p_factors(n):
	global primes
	to_test = [p for p in primes if p <= n**(0.5)]
	# print to_test
	p_factors = [1]
	for t in to_test:
		if n%t==0:
			n /= t
			p_factors.append(t)
			if n==1:
				return p_factors
	return p_factors

def phi(n):
	global primes
	q = 1
	phi = n
	prime_factors = list()
	test = [p for p in primes if p < n and p > q]
	# print test
	while True:
		if n == 1:
			break
		else:
			test = [p for p in primes if p < n and p > q]
			for t in test:
				if n%t==0:
					q = t
					n /= t
					prime_factors.append(t)
					while True:
						if n%t==0:
							n/=t
						else:
							break
	if len(prime_factors) > 1:
		for p in prime_factors:
			phi *= (1.0-1.0/float(p))
		return int(phi)
	else:
		return int(phi-1)

		

def is_perm(m,n):
	if m == n:
		return False
	else:
		s = [s for s in str(m)]
		t = [t for t in str(n)]
		for u in s:
			if u in t:
				t.remove(u)
			else:
				return False
		if len(t) == 0:
			return True
		else:
			return False

# primes = e_sieve(10000000)
# primes, comps = sieve(int(10000000**(0.5)))
primes, comps = sieve(int(10000000**(0.5)))

# construct a dict from this list of primes that makes number, totient pairs, then check their permutability

totient_perms = list()

for i in range(2,16):
	print i, phi(i)

# print phi(9)
print phi(87109)

# # for i in range(1,100000):
# for i in range(87109,87111):
# 	# print "i",i
# 	j = i
# 	to_test = [p for p in primes if p <= i**(0.5)]
# 	# print to_test
# 	totient = float(i-1)
# 	for t in to_test:
# 		if i%t==0:
# 			print i,t, i*(t-1)/t
# 			i/=t
# 			to_test = [p for p in primes if p <= i**(0.5)]
# 			totient *= ((t-1)/t)
# 	# totient -= 1.0
# 	tot = phi(i)
# 	if is_perm(i,tot):
# 		totient_perms.append((j,tot,float(i)/tot))
# 		print j,tot,float(i)/tot
# print totient_perms# for i in range(1,10000000):


# print primes

# totient_factors = dict()

# prime_combs = list()

# # for i in range(1,len(primes)+1):
# # 	prime_combs.append(list(itertools.combinations(primes,i)))

# print prime_combs,len(prime_combs)
# for e,p in enumerate(primes):
# 	for i in range(0,e+1):

# print primes

# print p_factors(9)

# print phi(9)

# print is_perm('16790','07619')
# for n in comps:
# 	p = phi(n)
# 	if is_perm(n,int(p)):
# 		print n, p, n/p

# for p in primes:
# 	facto
