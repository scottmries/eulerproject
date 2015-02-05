import math

amisums = 0

def amisum(n):
	bound = math.floor(math.sqrt(n))+1
	asum = 1;
	for i in range(2, bound):
		if n%i==0:
			asum = asum + i + n/i
	return asum

for i in range(1,10000):
	a = amisum(i);
	if a != i:
		if amisum(a)==i:
			print(a)
			print(i)
			amisums += a+i
			print(amisums)

print(amisums)
