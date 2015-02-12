import math
i = 3
primes = [2,3]
squares = [1,4]

def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

def is_square(i):
	return math.sqrt(i) == int(math.sqrt(i))

found = False

while not found:
	if not is_prime(i):
		for p in range(primes[-1],i):
			if is_prime(p):
				if p not in primes:
					primes.append(p)
		for s in range(squares[-1],i):
			if is_square(s):
				if s not in squares:
					squares.append(s)
		exception = True
		for p in primes:
			for s in squares:
				if 2*s+p == i:
					# print p, 2*s
					exception = False
					break
		if not exception:
			print "%s is not the exception." % (i)
		else:
			print "%s is the exception." % (i)
			found = True
	i+=2
