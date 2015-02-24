power = 1
solutions = list()

while len(str(9**power))<=power:
	base = 1
	while len(str(base**power))<=power:
		if len(str(base**power))==power:
			solutions.append([base,power])
			print base, power, base**power
		base += 1
	power += 1
	# Not entirely sure why 9**21 is the last one, but it is
	if power>21:
		print len(solutions)
		quit()
