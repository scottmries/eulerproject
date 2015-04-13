import math
maximum = 0
solution = 0

file = open("base_exp.txt")

for e,line in enumerate(file):
	base,exp=line.split(',')[0],line.split(',')[1]
	# taking the log brings the exponent down, the base is logged
	value = float(exp)*math.log(float(base))
	if value>maximum:
		maximum = value
		solution = e + 1

print solution
