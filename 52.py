import math
found = False
i = 1.0

def split_to_digits(n):
	digits = list()
	for s in str(n):
		digits.append(s)
	return digits

def test_digits(d,digits_lists,i,test_digit):
	global found
	if i < len(digits_lists):
		if digits_lists[i] == d:
			if digits_lists[i] < (len(digits_lists)-1):
				test_digits(d,digits_lists,i+1)
			else:
				print test_digit
				quit()

while not found:
# while i < 100:
	digits_lists = list()
	for j in range(1,7):
		digits_lists.append(split_to_digits(int(i*j)))
		digits_lists[j-1].sort()
	# print d0, d, d2
	sixth = i/(10.0**int(math.log(i,10)))
	if sixth < 10.0/6.0:
		test_digits(digits_lists[0],digits_lists,1,i)
	i+=1
