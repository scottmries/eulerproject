def count_rectangles(x,y):
	rect_sizes = [(i,j) for i in range(1,x+1) for j in range(1,y+1)]
	count = 0
	for size in rect_sizes:
		# print size, (x-(size[0]-1))*(y-(size[1]-1))
		count += (x-(size[0]-1))*(y-(size[1]-1))
	return count

print count_rectangles(3,2)

proximity = 2000000

for x in range(1,1001):
	for y in range(1,1001):
		count = count_rectangles(x,y)
		if abs(2000000-count)< proximity:
			proximity = abs(2000000-count)
			print x,y,x*y, proximity
			if proximity < 3:
				quit()
