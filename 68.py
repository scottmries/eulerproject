# construct all possible links that begin with 10 (has outer node 10 -- 10 will be outer otherwise the string would be 17 digits)
# from the remaining digits, construct all possible second links that have the same sum as the previous one, and have its last digit as its own second
# do this twice more
# for the last link, the last remaining digit, is outer, the previous's last digit is in the middle, and the first link's middle digit is last
# having generated all possible 16-digit magic fivegon rings, find the least outer element in each, and rotate so that the least is first, then compare


import itertools

fivegon_rings = list()
for p in [(10,)+p for p in list(itertools.permutations(range(1,10),2))]:
	middle = p[2]
	for s in [(a[0],middle,a[1]) for a in [q for q in list(itertools.permutations([r for r in range(1,10) if r not in p],2))] if sum([a[0],middle,a[1]])==sum(p)]:
		middle = s[2]
		for t in [(t[0],middle,t[1]) for t in [q for q in list(itertools.permutations([r for r in range(1,10) if r not in p and r not in s],2))] if sum([t[0],middle,t[1]])==sum(p)]:
			middle = t[2]
			for u in [(u[0],middle,u[1]) for u in [q for q in list(itertools.permutations([r for r in range(1,10) if r not in p and r not in s and r not in t],2))] if sum([u[0],middle,u[1]])==sum(p)]:
				v = ([r for r in range(1,10) if r not in p and r not in s and r not in t and r not in u][0],u[2],p[1])
				if sum(v)==sum(p):
					ring = (p,s,t,u,v)
					fivegon_rings.append(ring)
					print ring
					least_outer = 10
					first_i = 0
					for e,link in enumerate(ring):
						print "outer",link[0],e
						if link[0] < least_outer:
							least_outer = link[0]
							first_i = e
					print first_i
					fivegon_ring = ''
					for i in range(0,5):
						line = ring[(first_i+i)%5]
						for l in line:
							fivegon_ring+=str(l)
					fivegon_rings.append(int(fivegon_ring))

print fivegon_rings
print max(fivegon_rings)
