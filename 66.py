# x**2 - D*y**2 = 1 is the positive form of the Pell equation
# the minimal solution can be found by testing the sequence of convergents of D**(1/2) as h/k for h**2-D*k**2=1
# how to find the convergents?
# solve problem 64 first

# get the continued fraction of sqrt(D)
# make a list for the integers in the finite expansion to come
# while the solution is not found
# increase the expansion by one by iterating over list[i%len(list)+1]
# if h**2-D*k**2=1
# if h > max
# max = h
	

import math
from fractions import gcd

def solve_pell(D,exp):
	exp = sqrt_expansion(D)
	finite_exp = [exp[0],exp[1]]
	i = 1
	while True:
		(h,k) = conv_from_cont_frac(finite_exp)
		if h**2-D*k**2==1:
			print "Pell: D=%s h=%s k=%s" % (D,h,k)
			return (h,k)
		else:
			
			print "D=%s index=%s exp=%s h=%s k=%s" % (D,i%(len(exp)-1)+1, exp, h, k)
			finite_exp.append(exp[i%(len(exp)-1)+1])
			i += 1


def next_cont_frac(a,n,d):
		f = gcd(a*n+d,n)
		return(((a*n+d)/f,n/f))

def conv_from_cont_frac(cont_frac):
	rev = [r for r in reversed(cont_frac)]
	# print(rev)
	for e,i in enumerate(rev):
		if e == 0:
			next=next_cont_frac(rev[1],rev[0],1)
		elif e < len(rev) - 1:
			next=next_cont_frac(rev[e+1],next[0],next[1])
	return (next[0],next[1])

def next_simple_cf_term((x,y,z)):
	# input is (sqrt(x)-y)/z
	# take the highest integer below that quotient as an
	an = int(math.floor((math.sqrt(x)+y)/z))


	# sqrt(x) = an + (math.sqrt(x)+y-an*z)/z
	y -= an*z
	# sqrt(x) = an + (math.sqrt(x) +y)/z

	# z/(math.sqrt(x) + y)
	# z*(math.sqrt(x) - y)/(x-y**2)

	f = gcd(z,(x-y**2))
	z = (x-y**2)/f

	return (an,(x,abs(y),z))



def sqrt_expansion(n):
	args = (n,0,1)
	full_expansion = list()
	while True:
		# print args
		next_expansion = next_simple_cf_term(args)
		full_expansion.append(next_expansion[0])

		if next_expansion[0] == 2*full_expansion[0]:
			break
		else:
			args = next_expansion[1]
	return full_expansion

m = 0
solution = 0

def is_square(i):
	return math.floor(i**0.5)**2==i

for d in range(4,1001):
	if not is_square(d):
		# print d
		exp = sqrt_expansion(d)
		(h,k) = solve_pell(d,exp)
		if h > m:
			m=h
			solution = d
		m = max(m,h)
print solution
