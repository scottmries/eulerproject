import math

matches = list()

def check_match(u,v):
	if float(v)/float(u) == q:
				matches.append([j,i,int(v),int(u)])

def factors(x):
	factors = list()
	for i in range(2,int(math.sqrt(x)+1)):
		if x%i==0:
			factors.append(i)
			factors.append(x/i)
	return factors

def reduce(n,d):
	nfactors = factors(n)
	dfactors = factors(d)

	for f in nfactors:
		if f in dfactors:
			n /= f
			d /= f
	return [n,d]

for i in range(11,99):
	for j in range(11,i):
		# print "i %s j %s" % (i,j)
		q = float(j)/float(i)
		s,t = str(i), str(j)
		if i%10>1 and j%10>1:
			if s[0] == t[0]:
				u = s[1]
				v = t[1]
				check_match(u,v)
			elif s[0] == t[1]:
				u = s[1]
				v = t[0]
				check_match(u,v)
			elif s[1] == t[0]:
				u = s[0]
				v = t[1]
				check_match(u,v)
			elif s[1] == t[1]:
				u = s[0]
				v = t[0]
				check_match(u,v)
			
num, den = 1,1
for m in matches:
	num *= m[2]
	den *= m[3]

print reduce(num,den)[1]
