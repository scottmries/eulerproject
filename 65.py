import math
from fractions import gcd

# quite ugly, but it's correct

for k in range(2,101):
	e_exp = [2]
	for i in range(3,3+k-1):
		if i%3==1:
			e_exp.append(2*((i-1)/3))
		else:
			e_exp.append(1)

	def next_cont_frac(a,n,d):
		f = gcd(a*n+d,n)
		return(((a*n+d)/f,n/f))


	r_e_exp = [r for r in reversed(e_exp)]
	for e,i in enumerate(r_e_exp):
		if e == 0:
			next=next_cont_frac(r_e_exp[1],r_e_exp[0],1)
		elif e < len(r_e_exp)-1:
			next=next_cont_frac(r_e_exp[e+1],next[0],next[1])
print k, sum(int(digit) for digit in str(next[0]) if str(next[0]) != "L")
