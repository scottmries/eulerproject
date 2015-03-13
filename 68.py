# There will be five numbers, of 1-10
# Each successive pair of these numbers will be part of a line
# The remaining five numbers can be in any of the outer five circles
# If the sum of all the lines is the same
# Return the lines
# Sort the lines, concat to an int, and add to a list
# Find the maximum in the list

# No, this will take forever

import itertools

# all possible inner perms, excluding 10, which would cause a 17-digit number
inners = list(itertools.permutations(range(0,10),5))

print len(inners)

magics = list()

for p in inners:

	outers = list(itertools.permutations([o for o in range(0,11) if o not in inners]))

	for o in outers:

		lines = [(o[0],p[0],p[1]),(o[1],p[1],p[2]),(o[2],p[2],p[3]),(o[3],p[3],p[4]),(o[4],p[4],p[0])]

# a,b,c,d,e,v,w,x,y,z

# To guarantee a 16-digit solution, ten cannot be in the inner circle

# if p.index(10)>4:

	# lines = [(p[5],p[0],p[1]),(p[6],p[1],p[2]),(p[7],p[2],p[3]),(p[8],p[3],p[4]),(p[9],p[4],p[0])]
	# lines = [(v,a,b),(w,b,c),(x,c,d),(y,d,e),(z,e,a)]


		if all(sum(lines[l])==sum(lines[l-1]) for l in range(1,5)):
			s = ""
			m = min([l[0] for l in lines])
			i = 0
			while True:
				if lines[i][0]==m:
					break
				else: i += 1
			for l in range(i,i+5):
				for c in lines[l%5]:
					s += str(c)
			print s
			magics.append(int(s))

print max(magics)
