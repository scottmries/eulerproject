import math

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = e_sieve(10000)

def gcf(n,d):
	gcf = 1
	test_primes = [p for p in primes if p<=min(n,d)]
	for p in test_primes:
		while True:
			if n%p==0 and d%p==0:
				n /= p
				d /= p
				gcf*=p
			else:
				break
	return gcf

def next_simple_cf_term((x,y,z)):
	# input is (sqrt(x)-y)/z
	# take the highest integer below that quotient as an
	an = int(math.floor((math.sqrt(x)+y)/z))


	# sqrt(x) = an + (math.sqrt(x)+y-an*z)/z
	y -= an*z
	# sqrt(x) = an + (math.sqrt(x) +y)/z

	# z/(math.sqrt(x) + y)
	# z*(math.sqrt(x) - y)/(x-y**2)

	f = gcf(z,(x-y**2))
	z = (x-y**2)/f

	return (an,(x,abs(y),z))



def sqrt_expansion(n):
	args = (n,0,1)
	full_expansion = list()
	while True:
		next_expansion = next_simple_cf_term(args)
		full_expansion.append(next_expansion[0])

		if next_expansion[0] == 2*full_expansion[0]:
			break
		else:
			args = next_expansion[1]
	return full_expansion

# for all quadratic irrationals, the first non-repeating number is floor(sqrt(x))
# 	and the last of the period is 2*floor(sqrt(x)).
# 	a quality of the digits between these is that they are symmetrical,
# 	but the appearance of 2*floor(sqrt(x)) may be sufficient?

def is_square(i):
	return math.floor(i**0.5)**2==i

solution = 0

for i in range(1,10001):
	if not is_square(i):
		print sqrt_expansion(i)
		if (len(sqrt_expansion(i))-1)%2==1:
			solution += 1

print solution
