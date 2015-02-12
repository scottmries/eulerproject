# NOT EVEN REMOTELY EFFICIENT

import math

def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

def unique_prime_factors(n):
	factors = list()
	primes = [2,3]
	for i in range(2,n):
		divisible = True
		while divisible:
			if n%i==0:
				if not i in factors:
					factors.append(i)
				n /= i
			else:
				divisible = False
		else:
			continue
	return factors


i = 1000
while True:
	if not is_prime(i):
		print(i)
		if len(unique_prime_factors(i))==4:
			if not is_prime(i+1):
				if len(unique_prime_factors(i+1))==4:
					if not is_prime(i+2):
						if len(unique_prime_factors(i+2))==4:
							if not is_prime(i+3):
								if len(unique_prime_factors(i+3))==4:
									print i
									quit()
								else:
									i+=4
							else:
								i+=4
						else:
							print i
							i+=3
					else:
						i+=3
				else:
					i+=2
			else:
				i+=2
		else:
			i+=1
	else:
		i+=1
