# 10 must be on the outer ring, otherwise the string would be 17-digits
# The highest possible starting number is 6
# From the example, it appears that a high solution corresponds to a low total
# The lowest possible total is 13 (10+1+2), the highest is 27
# How many ways are there to construct a 13-total line beginning with 6? 4
# Of those four, is it possible to construct a magic ring around any of them?
# If not, let's try 14

# for s in rev(range(1,7)):
# 	for t in range(13,28):
# 		starting_rings = [(s,i,j) for i,j in range(1,11) if s+i+j == t and i != j and j != s and i != s]


# There will be five numbers, of 1-10
# Each successive pair of these numbers will be part of a line
# The remaining five numbers can be in any of the outer five circles
# If the sum of all the lines is the same
# Return the lines
# Sort the lines, concat to an int, and add to a list
# Find the maximum in the list

# No, this will take forever

import itertools

fivegon_rings = list()
# print type([10])
# print type([list(itertools.permutations(range(1,10),2))])
for p in [(10,)+p for p in list(itertools.permutations(range(1,10),2))]:
	middle = p[2]
	# print p
	# print list(itertools.permutations([r for r in range(1,10) if r not in p]))
	for s in [(a[0],middle,a[1]) for a in [q for q in list(itertools.permutations([r for r in range(1,10) if r not in p],2))] if sum([a[0],middle,a[1]])==sum(p)]:
		middle = s[2]
		print p,s
		for t in [(t[0],middle,t[1]) for t in [q for q in list(itertools.permutations([r for r in range(1,10) if r not in p and r not in s],2))] if sum([t[0],middle,t[1]])==sum(p)]:
			middle = t[2]
			# print t
			for u in [(u[0],middle,u[1]) for u in [q for q in list(itertools.permutations([r for r in range(1,10) if r not in p and r not in s and r not in t],2))] if sum([u[0],middle,u[1]])==sum(p)]:
				# print u
				v = ([r for r in range(1,10) if r not in p and r not in s and r not in t and r not in u][0],u[2],p[1])
				# print p,s,t,u,v
				if sum(v)==sum(p):
					ring = (p,s,t,u,v)
					fivegon_rings.append(ring)
					print ring
					first_i = 10
					for e,link in enumerate(ring):
						if link[0] < first_i:
							first_i = e
					fivegon_ring = ''
					for i in range(0,5):
						line = ring[(first_i+i)%5]
						for l in line:
							fivegon_ring+=str(l)
					fivegon_rings.append(int(fivegon_ring))

print fivegon_rings
print max(fivegon_rings)


# all possible inner perms, excluding 10, which would cause a 17-digit number
# inners = list(itertools.permutations(range(1,11),5))

# print inners

# magics = list()

# for p in inners:

# 	outers = list(itertools.permutations([o for o in range(0,11) if o not in inners]))

# 	for o in outers:

# 		lines = [(o[0],p[0],p[1]),(o[1],p[1],p[2]),(o[2],p[2],p[3]),(o[3],p[3],p[4]),(o[4],p[4],p[0])]

# # a,b,c,d,e,v,w,x,y,z

# # To guarantee a 16-digit solution, ten cannot be in the inner circle

# # if p.index(10)>4:

# 	# lines = [(p[5],p[0],p[1]),(p[6],p[1],p[2]),(p[7],p[2],p[3]),(p[8],p[3],p[4]),(p[9],p[4],p[0])]
# 	# lines = [(v,a,b),(w,b,c),(x,c,d),(y,d,e),(z,e,a)]


# 		if all(sum(lines[l])==sum(lines[l-1]) for l in range(1,5)):
# 			s = ""
# 			m = min([l[0] for l in lines])
# 			i = 0
# 			while True:
# 				if lines[i][0]==m:
# 					break
# 				else: i += 1
# 			for l in range(i,i+5):
# 				for c in lines[l%5]:
# 					s += str(c)
# 			print s
# 			magics.append(int(s))

# print max(magics)
