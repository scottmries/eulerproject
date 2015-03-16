import math

# sqrt(x)
# floor(sqrt(x)) + sqrt(x) - floor(sqrt(x))
# floor(sqrt(x)) + 1/(1/(sqrt(x)-floor(sqrt(x)))) = floor(sqrt(x)) + 1/(sqrt(x)-(sqrt(x)+floor(sqrt(x))/(sqrt(x)**2-(floor(sqrt(x)))**2))

# for 1/(sqrt(23)-4), input is (23,4,1), output is (1,23,3,7)
def root_denom(x,y,z):
	# 1/(x**(1/2)-y) => (x**(1/2)+y)/(x-y**2) => floor((x**(1/2)+y)/(x-y**2)) + (x**(1/2)-y**2*(floor((x**(1/2)+y)/(x-y**2))))
	print x,y,x-y**2
	a = (x**(1/2)+y)/(x-y**2)
	b = x
	c = y**2*(x**(1/2)+y)
	d = x-y**2
	return (a,b,c,d)

# for all quadratic irrationals, the first non-repeating number is floor(sqrt(x))
# 	and the last of the period is 2*floor(sqrt(x)).
# 	a quality of the digits between these is that they are symmetrical,
# 	but the appear of 2*floor(sqrt(x)) may be sufficient?

print (9**(1/2))
print (10**(1/2))

solution = 0

# for i in range(1,10000):
for i in range(1,10):
	expansion = [i**(1/2)]
	args = [i,i**(1/2),1]
	while True:
		next_result = root_denom(args[0],args[1],args[2])
		expansion.append(next_result[0])
		print expansion
		if next_result[0] == 2*i**(1/2):
			length = len(expansion)-1
			if length%2==0:
				solution += 1
			print "expansion of %s is %s" % (i,"["+expansion[0]+","+expansion[1:]+"]")
			break
		else:
			args = [next_result[1],next_result[2],next_result[3]]

