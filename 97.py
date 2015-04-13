solution = 1
for i in range(1,7830458):
	solution *= 2
	if solution > 10**10:
		solution = int(str(solution)[-10:])
solution *= 28433
print str(solution + 1)[-10:]
