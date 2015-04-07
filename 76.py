total = 100
coins = range(1,100)
grid = [1] + [0]*total

for c in coins:
	for i in range(c,total+1):
		grid[i] += grid[i-c]

print grid[total]
