import itertools, math

primes = list()

matched_3_or_more = list()

def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True

def split_to_digits(n):
	digits = list()
	for s in str(n):
		digits.append(s)
	return digits

def concat_to_int(list):
	s = ""
	for l in list:
		s+=l
	return int(s)

for i in range(1000,10000):
	if is_prime(i):
		primes.append(i)
# print primes
for p in primes:
	perms = list(itertools.permutations(split_to_digits(p)))
	# print perms
	matched = list()
	for pm in set(perms):
		if concat_to_int(pm) in primes:
			matched.append(pm)
	# print matched
	if len(matched) > 3:
		matched_3_or_more.append(matched)
for m in matched_3_or_more:
	m.sort()
	s = list()
	for n in m:
		s.append(concat_to_int(n))
	# print s

	for e,i in enumerate(s):
		if e < len(s)-1:
			diff = s[e+1]-s[e]
			if (s[e+1]+diff) in s:
				print s[e],s[e+1],s[e+2], diff
