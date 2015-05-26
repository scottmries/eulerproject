ratio = 0.0

i = 100.0

bouncies = 0.0

def is_bouncy(n):
	a_digit_increases = False
	a_digit_decreases = False
	for e, digit in enumerate(str(n)[:-1]):
		if int(digit) > int(str(n)[e+1]):
			a_digit_decreases = True
		if int(digit) < int(str(n)[e+1]):
			a_digit_increases = True
		if a_digit_increases and a_digit_decreases:
			return True
	return False

print is_bouncy(155349)

while True:
	if ratio < 0.99:
		print int(i)
		if is_bouncy(int(i)):
			bouncies += 1.0
			print i, ratio
		ratio = bouncies/i
		i += 1.0
	else:
		print i
		quit()
