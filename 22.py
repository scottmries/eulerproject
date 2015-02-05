import math

abusums = 0

def abusum(n):
	bound = math.floor(math.sqrt(n))+1
	asum = 1;
	for i in range(2, bound):
		if n%i==0:
			asum = asum + i + n/i
	if asum > n:
		return asum
	else:
		return 0

for i in range(1,28123):
	abusums += abusum(i)

print(abusums)
