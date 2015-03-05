solution = 0
chain_lengths = dict()

def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		n*factorial(n-1)
		return n*factorial(n-1)

def factorial_link(n):
	link = 0
	for c in str(n):
		link += factorial(int(c))
	return link

print factorial(5)
print factorial_link(169)

for i in range(1,1000001):
	chain = [i]
	last_link = factorial_link(i)
	if i%5000==0:
		print i, len(chain_lengths)
	while True:
		if last_link in chain_lengths:
			chain_length = chain_lengths[last_link] + len(chain)
			if chain_length==60:
				print "a 60! %s" % i
				solution+=1
				chain_lengths[i] = chain_length
				break
			else:
				chain_lengths[i] = chain_length
				break
		else:
			if last_link in chain:
				first_instance = chain.index(last_link)
				# print last_link, first_instance
				if i < 10:
					print i, first_instance, len(chain), len(chain)-first_instance
				if len(chain) == 60:
					print "a 60! %s" % i
					chain_lengths[i] = len(chain)
					solution += 1
					break
				else:
					chain_lengths[i] = len(chain)
					break
			else:
				chain.append(last_link)
				last_link = factorial_link(last_link)


print solution
