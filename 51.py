# this one's a doozy, and it's still not done....

# generate the primes
# how to determine membership in a family
# all digits will be the same except one, at least once but not necessarily always, and it will always be different in the same way


def lowest_dig(m):
	return min([int(s) for s in str(m)])


def fam_mem(m,n):
	if len(str(m)) != len(str(n)):
		return False
	diffs = list()
	for e,s in enumerate(str(m)):
		diff_code = (int(s) - int(str(n)[e]))
		diffs.append(diff_code)
	if diffs[-1]>0:
		return False
	else:
		m_code = ''
		n_code = ''
		
		
		if len(set(s for s in diffs))==2:
			s = ''
			for d in diffs:
				if abs(d)>0:
					s+='1'
				else:
					s+='0'
				
		else:
			return False
		m_switched_digits = list()
		n_switched_digits = list()
		for e,d in enumerate(s):
			if int(d)>0:
				m_switched_digits.append(int(str(m)[e]))
				n_switched_digits.append(int(str(n)[e]))

		
		if max(set(m_switched_digits)) > 2:
			return False

		else:
			# print set(m_switched_digits),set(n_switched_digits)
			
			if len(list(set(m_switched_digits)))==1 and len(list(set(n_switched_digits)))==1:
				# this is a string of ones and zeroes showing the locations of replacement from the smaller to larger number
				# it guarantees that the replaced digits were identical
				print list(set(m_switched_digits)), list(set(n_switched_digits))
				return s
			else:
				return False

def e_sieve(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

# print fam_mem(56003,56443)
# print fam_mem(56003,56103)
# print fam_mem(56003,56113)
# print fam_mem(56003,56333)
# print fam_mem(56663,56003)
# print fam_mem(56773,56003)
# print fam_mem(56993,56003)
# print fam_mem(56063,56603)


primes = [p for p in e_sieve(1000000) if p > 100000]
# print primes

checked = dict()


for e,p in enumerate(primes):
	if lowest_dig(p)<3:
		print p, len(checked)
		to_test = [q for q in primes if q >= p]
		family = dict()
		for q in to_test:
			fam = fam_mem(p,q)
			if fam != False:
				if q in checked:
					if fam in checked[q]:
						continue
					else:
						checked[q].append(fam)
						if fam in family:
							family[fam].append(q)
							fam_size = len(family[fam])
							if fam_size > 3:
							# if p == 56003:
								print p,family[fam_mem(p,q)]
								if fam_size == 8:
									print "solution!"
									quit()
						else:
							family[fam] = [p,q]
							if p == 56003:
								print family
				else:
					checked[q]=[fam]
