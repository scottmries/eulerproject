import itertools

# explanation:
# how many changing digits must there be?
# if there are one or two changing digits,
# their sum%3 will be 0,1, or 2, and their addition%3 to the unchanging digits must not be zero
# there are not enough combinations available for this to be possible

# there must be three changing digits: they can be any of the ten digits without affecting the 3-divisibility of the overall digit

# the sum%3 of the unchanging digits must therefore != 0

nc = [[h for h in str(i)] for i in range(100,1000) if i%3!=0]

# assuming a string 'xxxxx', get all the positions of the non-changing digits

ncp = list(itertools.combinations(range(0,5),2))
print ncp

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = [p for p in e_sieve(1000000) if p >=100000]

# given the string with exes and digits, return the prime occurences of its family

def test(n):
	l = list()
	for i in range(10):
		t = ''
		for s in n:
			# print s
			if s=='x':
				t += str(i)
			else:
				t += s
		# print t
		t = int(t)
		if t in primes:
			l.append(t)
	return [k for k in l if k in primes]

# print test('56xx3')

for m in ncp:
	for n in nc:
		s = ""
		t_sum = 0
		while True:

			# generate the string with exes and digits, except the last digit
			
			if len(s)<=len(n)+1:
				if len(s) in m:
					e = m.index(len(s))
					t_sum += int(n[e])
					s+=n[e]
				else:
					s+='x'
			else:
				break
		
		# the last digit can only be 1,3,7, or 9 (all other endings are sufficient for divisibility), 
		# and the total non-changing digits must not be 3-divisible

		jl = [s+str(k) for k in [1,3,7,9] if (k + t_sum)%3!=0]
		for s in jl:
			result = test(s)
			if len(result)>5:
				print len(result),result
				if len(result)>7:
					quit()
