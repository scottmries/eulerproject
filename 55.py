lychrels = list()

def concat_to_int(list):
	s = ""
	for l in list:
		s+=l
	return int(s)

def split_to_digits(n):
	digits = list()
	for s in str(n):
		digits.append(s)
	return digits

def rev_sum(n):
	return concat_to_int(reversed(split_to_digits(n)))+n

def is_palindrome(n):

	return split_to_digits(n) == split_to_digits(n)[::-1]

for i in range(1,10001):
	test = i
	j = 1
	lychrel = True
	while j < 50 and lychrel == True:
		if is_palindrome(rev_sum(test)):
			lychrel = False
		else:
			j += 1
			test = rev_sum(test)
	if lychrel == True:
		lychrels.append(i)
		print i

print len(lychrels), lychrels
