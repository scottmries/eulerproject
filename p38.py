pandigitals = list()

def split_to_digits(n):
	digits = list()
	for s in str(n):
		digits.append(s)
	return digits

for i in range(1,50000):
	concat_prod = str(i)
	d = split_to_digits(i)
	# Check for uniqueness in the digits; non-uniques multiplied by one can be filtered
	if len(set(d)) == len(d):
		# print d, i
		j = 2
		while len(concat_prod)<10:
			concat_prod += str(j*i)
			
			j+=1
			# Check for uniqueness in the concatenated digits
			e = split_to_digits(int(concat_prod))
			if len(set(e)) == len(e) and len(e) == 9 and not '0' in e:
				pandigitals.append([i,int(concat_prod)])
				print concat_prod
m = 0
for p in pandigitals:
	if p [1] > m:
		m= p[1]

print m
