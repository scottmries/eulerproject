import math

def make_primes_list_below(n):
	primes = [2]
	for i in range(3,n+1):
		for p in primes:
			if i%p==0:
				is_prime=False
				break;
			else:
				is_prime=True
		if is_prime:
			primes.append(i)
			primes.append(-1*i)
	return primes

def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

primes = make_primes_list_below(1000)

max = 0
h = 0

print(primes)

# only the primes need tested because i = 0 is valid
for a in primes:
	for b in primes:
		if b != 0:
			i = 0
			while True:
				q = i*i+a*i+b
				if is_prime(abs(q)):
					i += 1
				else:
					if i > max:
						max = i
						h = a*b
						print a,b,h, max
						break
					else:
						break

print(h)
