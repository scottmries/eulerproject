divisible_strings = list()

divisor_array = [13,11,7,5,3,2]

final_sum = 0

def split_to_digits(n):
	digits = list()
	for s in str(n):
		digits.append(s)
	return digits

def test_divisible_strings(strings,divisor_array,index):
	divisor = divisor_array[index]
	print divisor
	print(strings)
	new_strings = list()
	for i in strings:
		digits = split_to_digits(int(i))
		if len(set(digits)) == len(digits):
			sub = str(i)[0:2]
			for j in range(0,10):
				test_sub = str(j)+sub
				test_sub_digits = split_to_digits(test_sub)
				if len(set(test_sub_digits)) == len(test_sub_digits):
					if int(test_sub)%divisor == 0:
						entry = str(j)+str(i)
						new_strings.append(entry)
	if index+1 < len(divisor_array):
		test_divisible_strings(new_strings,divisor_array,index+1)
	else:
		final_strings = list()
		# final_sum = 0
		for n_s in new_strings:
			n_s_digits = split_to_digits(n_s)
			if len(set(n_s_digits)) == len(n_s_digits):
				for k in range(0,10):
					if not str(k) in n_s_digits:
						print n_s_digits, k
						final_str = str(k) + n_s
						if len(set(split_to_digits(int(final_str)))) == len(split_to_digits(int(final_str))):
							final_strings.append(final_str)
							# final_sum += int(final_str)
		print final_strings
		final_sum = 0
		for f_s in final_strings:
			final_sum += int(f_s)
		print final_sum


for i in range(100,1000):
	digits = split_to_digits(i)
	if i%17==0 and len(set(digits)) == len(digits):
		divisible_strings.append(i)

test_divisible_strings(divisible_strings,divisor_array,0)
