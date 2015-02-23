solution = 0

def expansion(m):
	if m == 1:
		return (3,2)
	else:
		#add the previous numerator and denominator for the denominator
		#add the previous numerator and twice the denominator for the numerator
		p = expansion(m-1)
		return (p[0]+p[1]*2,p[0]+p[1])

for i in range(1,1000):
	e = expansion(i)
	n = e[0]
	d = e[1]
	print "i %s n %s d %s" % (i,n,d)
	if len(str(n)) > len(str(d)):
		solution += 1

print solution
