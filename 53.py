count = 0

def fac(n):
	total = 1
	for i in range(1,n+1):
		total *= i
	return total

def combinations(n,r):
	return fac(n)/(fac(r)*(fac(n-r)))

for i in range(1,101):
	for j in range(1,i+1):
		if combinations(i,j) > 1000000:
			count += 1

print count
