import sys, math

def pent(n):
	return n*(3*n-1)/2

def tri(n):
	return n*(n+1)/2

def hex(n):
	return n*(2*n-1)

def is_int(n):
	if n - int(n) > 0:
		return False
	return int(n)

def is_pent(P):
	n = (math.sqrt((24*P)+1)+1)/6
	return is_int(n)

def is_tri(T):
	n = (-1 + math.sqrt(1 + 8*T))/2
	return is_int(n)

def is_hex(H):
	n = (1 + math.sqrt(1 + 8*H))/4
	return is_int(n)

i = 286

while True:
	if is_pent(tri(i)):
		if is_hex(tri(i)):
			print tri(i)
			break
		else:
			i+=1
	else:
		i+=1
# for e in [1,3,6,10,11]:
# 	print(is_tri(e))

# for e in [1,5,12,22,23]:
# 	print(is_pent(e))

# for e in [1,6,15,28,29]:
# 	print(is_hex(e))



# T = n(n+1)/2

# P = n(3n-1)/2

# H = n(2n-1)

# n**2 + n - 2*T = 0

# 3*n**2 - n - 2*P = 0

# 2*n**2 - n - H = 0

# (-1 + math.sqrt(1 + 8*T)/2 = n

# (1 + math.sqrt(1 + 24*P))/6 = n

# (1 + math.sqrt(1 +8*H))/4 = n
