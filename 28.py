# at cycle n around the circle, the corners are 2*n apart

def get_corners_in_layer(n):
	last_corner = 1
	corners = [1]
	for i in range(1,n):
		last_corner = corners[-1]
		corners = [last_corner + i*2*j for j in range(1,5)]
	s = sum(corners)
	return [corners,s]

total = 0

for i in range(1,502):
	print get_corners_in_layer(i)[0]
	total += get_corners_in_layer(i)[1]

print total
