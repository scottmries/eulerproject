import math

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
	return primes

def get_corners_in_layer(n):
	last_corner = 1
	corners = [1]
	for i in range(1,n):
		last_corner = corners[-1]
		corners = [last_corner + i*2*j for j in range(1,5)]
	s = sum(corners)
	return [corners,s]

def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

primes = sieve(50000)

ratio = 1.0

prime_corners = 0.0

corners = 1.0

i = 0

last_corner = 1
while ratio >= 0.1:
	i += 1
	local_corners = [last_corner + i*2*j for j in range(1,5)]
	for e, l in enumerate(local_corners):
		# if e != 1:
		if l in primes or is_prime(l):
			prime_corners += 1.0
	corners += 4.0
	last_corner = local_corners[-1]
	ratio = prime_corners/corners
	print prime_corners, corners, ratio


print 2*i+1
