# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation

# current value

c = 0

# part of the root found so far

p = 0

# x is the greatest digit such that x(20p + x) <= c
# y = x(20p + x)

digit_sum = 0



for non_square in [x for x in range(1,100) if x not in map(lambda y: y*y, range(1,10))]:
	# print i
	expansion = [str(non_square)] + ['00'] * 100
	solution = ['']*100

	c = int(expansion[0])
	p = 0

	for e, digit in enumerate(expansion[:-1]):
		# c = int(digit)
		x = 0
		while True:
			# print x * (20*p + x), c
			if x * (20*p + x) > c or x > 9:
				break
			else:
				x += 1
		x -= 1
		solution[e] = int(x)
		y = x * (20*p + x)
		c -= y
		c = 100*c + int(expansion[e+1])
		p = 10*p + x
	print non_square, sum(solution)
	digit_sum += sum(solution)

print digit_sum
