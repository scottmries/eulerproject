# this one's a doozy, and it's still not done....

# we know that the last digit cannot be one of the ones that changes (only 1,3,7, and 9 can end a prime; there aren't 8 possibilities)

# s = sum of the non-changing digits

# t = the replacing digit

# s%3   t    	2*t 		3*t

# 0		t%3!=0	(2*t)%3!=0  impossible!
# 1		t%3!=2	(2*t)%3!=1
# 2		t%3!=1	(2*t)%3!=2
