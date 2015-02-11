import itertools, math

print list(itertools.permutations([0,1,2]))

m = 0

def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return False
	return True
for i in range(3,10):
	print i

for i in range(3,10):
	digits = []
	for j in range(1,i+1):
		digits.append(j)
		iterations = list(itertools.permutations(digits))
		for k in iterations:
			s = ""
			for l in k:
				s += str(l)
			if is_prime(float(s)):
				# print(s)
				if int(s) > m:
					m = int(s)
					print s

print(m)
