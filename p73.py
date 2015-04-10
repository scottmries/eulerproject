fractions = dict()
print fractions
solution = 0

limit = 12000

def sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = sieve(limit)

def uniq_prime_fac(n):
	factors = set()
	i = 0
	while True:
		if n > 1:
			if i >= len(primes):
				factors.add(n)
				return list(factors)
			if n%primes[i]==0:
				factors.add(primes[i])
				# print i, n,primes[i]
				n/=primes[i]
			else:
				i += 1
		else:
			break

	return list(factors)

facs = [uniq_prime_fac(l) for l in xrange(1,limit+1)]

def has_factors(n,list):
	for l in list:
		if n%l==0:
			return False
	return True


for e, p in enumerate(facs):
	print e+1,p
	e += 1
	fractions[e]=list()
	if e > 0:
		for g in xrange(1,e):
			print e,p,g
			if float(g)/float(e) < 0.5 and float(g)/float(e) > 1.0/3.0:
				# print g,p
				if has_factors(g,p):	
					fractions[e]+=(g,)
					solution += 1
				
			else:
				continue

print facs
print fractions
print solution
