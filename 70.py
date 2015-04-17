# phi(n) must be smaller than n but have the same number of digits as n, so only those permutations should be considered

# *** since phi(n) = n* product(1-1/p) for all distinct prime factors in n
# *** n must have as few distinct prime factors as possible
# *** and those distinct prime factors should be as high as possible (but cannot be higher than sqrt(n))
# *** but since phi(p) = p - 1 with p prime, n cannot be prime, as no pair n and n-1 will be permutations

from operator import mul
import itertools

def sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

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

upper_bound = 10000000

print upper_bound**0.5

ratio = 10.0

solution = (1,1,1)

primes = sieve(5000000)

phi_map = dict()

for p in reversed(primes):
	# print p
	phi_map[p] = p-1
	temp_phis = phi_map.keys()
	for phi in temp_phis:
		multiplier = p
		print p, phi
		while True:
			if multiplier*phi < upper_bound:
				phi_map[p*phi] = phi_map[p]*phi_map[phi]
				multiplier *= p
				if is_perm(p*phi,phi_map[p*phi]):
					if float(p*phi)/float(phi_map[p*phi]) < ratio:
						ratio = float(p*phi)/float(phi_map[p*phi])
						solution = (p*phi, phi_map[p*phi], ratio)
						print p*phi,phi_map[p*phi],ratio
			else:
				break

print len(phi_map.keys())
# print phi_map
print solution
