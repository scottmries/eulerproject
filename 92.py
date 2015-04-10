import itertools 

def next_link(n):
	t = 0
	for s in str(n):
		t += int(s)**2
	return t

next_links = [0]*10000001

solution = 0


print next_links

for e,n in enumerate(next_links):
	print e,n
	if e > 0 and n == 0:
# for n in next_links:
		i = e
		chain = list()
		while True:
			print i
			if i == 89:
				print "we're 89, chain: ",chain
				solution += 1
				for l in chain:
					l = "%03d" % l
					print l
					perms = list(itertools.combinations(str(l),len(str(len(next_links)))-1))
					print perms
					for p in perms:
						s = ''
						for q in p:
							s += q
						s = int(s)
						next_links[s] = 89
				break
			elif i == 1:
				for l in chain:
					l = "%03d" % l
					perms = list(itertools.permutations(str(l),len(str(len(next_links)))-1))
					for p in perms:
						s = ''
						for q in p:
							s += q
						s = int(s)
						# print s
						next_links[s] = 1
				break
			else:
				chain.append(i)
				i = next_link(i)
print next_links,solution
