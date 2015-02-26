# only check those n,d pairs where 2/5 < n/d < 3/7

import operator, math, collections
reduced_pairs = [[2.0/5.0,2,5],[3.0/7.0,3,7]]
print 3.0/7.0

def primes_to(n):
	primes = [x for x in range(2,n+1)]
	for i in range(2,int(math.sqrt(n)+1)):
		for p in primes:
			if(i*p) in primes:
				primes.remove(i*p)
	return primes

primes = primes_to(1000)

print primes

def reduce(a,b):
	hcf = 1
	for p in primes:
		if a%p==0 and b%p==0:
			hcf*=p
	return (a/hcf,b/hcf)

for d in range(1,1000001):
	range_n = reduced_pairs[0][1]
	range_d = reduced_pairs[0][2]
	for n in range(range_n*d/range_d,3*d/7):
		# make this happen dynamically
		# add to the list, sort it, and then refactor the range, only taking what falls between the element next to 3/7 and 3/7
		reduced_pairs.append([float(n)/float(d),reduce(n,d)[0],reduce(n,d)[1]])
		reduced_pairs = sorted(reduced_pairs)
		reduced_pairs.pop(0)

print reduced_pairs[0][1]
