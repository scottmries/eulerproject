tris = [(str(x*(x+1)/2)) for x in range(1,10000) if x*(x+1)/2 > 1000 and x*(x+1)/2 < 10000]
sqs = [(str(x**2)) for x in range(1,10000) if x**2 > 1000 and x**2 < 10000]
pens = [(str(x*(3*x-1)/2)) for x in range(1,10000) if x*(3*x-1)/2 > 1000 and x*(3*x-1)/2 < 10000]
hexs = [(str(x*(2*x-1))) for x in range(1,10000) if x*(2*x-1) > 1000 and x*(2*x-1) < 10000]
hepts = [(str(x*(5*x-3)/2)) for x in range(1,10000) if x*(5*x-3)/2 > 1000 and x*(5*x-3)/2 < 10000]
octs = [(str(x*(3*x-2))) for x in range(1,10000) if x*(3*x-2) > 1000 and x*(3*x-2) < 10000]

solution = 0
# figurates
figs = [(sqs,"s"),(pens,"p"),(hexs,"x"),(hepts,"h"),(octs,"o")]

# haha
fig_tree = ["t"+t for t in tris]

# appending around the list of figs five times guarantees we won't miss a combination
for f in 5*figs:
	# in each of the actual figurate values
	for g in f[0]:
		# get all the last branches
		fig_branches = [x[-2:] for x in fig_tree]
		for e,b in enumerate(fig_branches):
			# if the last branch matches the beginning of a new one
			if g[:2] == b:
				# and the identifying char for the figurate hasn't yet been encoding into the tree
				if f[1] not in fig_tree[e]:
					branch = fig_tree[e]+f[1]+g
					# add the branch
					fig_tree.append(branch)
					# if there are six branches and they're cyclical (last two are first two)
					if len(branch) == 30 and branch[-2:]==branch[1:3]:
						# sum the integer values
						solution = sum([int(branch[5*i+1:5*i+5]) for i in range(0,6)])
						# show us
						print branch, solution
						# eat figs
						quit()
