def is_a_right_triangle_with_the_origin(x1, y1, x2, y2):
	sides_squared = [(x1**2+y1**2), (x2**2+y2**2), ((x1-x2)**2+(y1-y2)**2)]
	# print sides_squared, 
	if any([side == 0 for side in sides_squared]):
		return False
	hypotenuse = max(sides_squared)
	sides_squared.remove(hypotenuse)
	return hypotenuse == sides_squared[0] + sides_squared[1]

limit = 50
solution = 0

coordinates = [(x,y) for x in range(0, limit + 1) for y in range(0, limit + 1)]

for e, coordinate in enumerate(coordinates):
	for coor_2 in coordinates[:e]:
		x1, y1 = coordinate
		x2, y2 = coor_2
		if is_a_right_triangle_with_the_origin(x1, y1, x2, y2):
			solution += 1
			print '(%s, %s), (%s, %s), %s' % (x1, y1, x2, y2, [(x1**2+y1**2), (x2**2+y2**2), ((x1-x2)**2+(y1-y2)**2)])

print solution
