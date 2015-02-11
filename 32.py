products = list()
pandigitals = list()

def split_to_digits(n):
	digits = list()
	for s in str(n):
		digits.append(s)
	return digits

def has_unique_digits(n):
	return len(set(n)) == len(n)

product_sum = 0

for i in range(1,5000):
	d = split_to_digits(i)
	if has_unique_digits(d) and "0" not in d:
		for j in range(1,5000):
			if len(str(i)) + len(str(j)) + len(str(i*j)) == 9:
				e = split_to_digits(j)
				if has_unique_digits(e) and "0" not in e:
					f = split_to_digits(i*j)
					if has_unique_digits(f) and "0" not in f:
						all_digits = d+e+f
						if has_unique_digits(all_digits):
							pandigitals.append([i,j,i*j])
							products.append(i*j)
for p in set(products):
	product_sum += p
print pandigitals
print set(products)
print product_sum
