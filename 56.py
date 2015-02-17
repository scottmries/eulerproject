m = 0

def sum_digits(n):
	sum = 0
	for s in str(n):
		sum += int(s)
	return sum

for i in range(1,101):
	for j in range(1,101):
		s = sum_digits(i**j)
		if s>m:
			m=s
			print m
