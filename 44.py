import sys

def pent(n):
	return n*(3*n-1)/2
pents = list()

for i in range(1,5000):
	pents.append(pent(i))
for p in pents:
	for q in pents:
		if (p+q) in pents and abs(p-q) in pents:
			print(abs(p-q))
			quit()
