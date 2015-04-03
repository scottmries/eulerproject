import itertools

nc = [[h for h in str(i)] for i in range(100,100000) if i%3!=0]
# print nc
ncp = list(itertools.combinations(range(0,5),3))
print ncp

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = [p for p in e_sieve(10000000) if p >=100000]

def test(n):
	l = list()
	for i in range(10):
		t = ''
		for s in str(n):
			if s=='x':
				t += str(i)
			else:
				t += s
		t = int(t)
		if t in primes:
			l.append(t)
	return [k for k in l if k in primes]

for m in ncp:
	for n in nc:
		s = ""
		t_sum = 0
		while True:
			if len(s)<=len(n):
				for e,o in enumerate(m):
					# print o
					if len(s) == o:
						# print s,m,o
						t_sum += int(n[e])
						s+=n[e]
					else:
						s+='x'
			else:
				break
		print s
		jl = [s+str(k) for k in [1,3,7,9] if (k + t_sum)%3!=0]
		for s in jl:
			result = test(s)
			if len(result)>3:
				# print len(result),result
				if len(result)>7:
					quit()
