def find_cycle(n):
	p = len(str(n))
	# first remainder digits, long division style
	remainders = [10**p%n]
	while True:
		# next remainder digits, long division style
		r = (remainders[-1])*10**p%n
		if r in remainders:
			length = len(remainders) - remainders.index(r)
			return [n, length]
			break
		else:
			remainders.append(r)

m = 0
for i in range(1,1001):
	if find_cycle(i)[1] > m:
		print find_cycle(i)[0]
		m = find_cycle(i)[1]
