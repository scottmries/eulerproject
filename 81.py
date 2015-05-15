matrix_file = open('matrix.txt')
matrix = list()
for line in matrix_file:
	cells = line.split(',')
	row = list()
	for cell in cells:
		cell = cell.replace('\n','')
		row.append(cell)
	matrix.append(row)

minimum_paths_sums = matrix

ordered_coordinates = [(distance_from_right,distance_from_corner - distance_from_right) 
	for distance_from_corner in xrange(0,len(matrix)+len(matrix[0])) 
	for distance_from_right in xrange(0,distance_from_corner+1) 
	if distance_from_right < len(matrix) and (distance_from_corner - distance_from_right) < len(matrix)]

for ordered_coordinate in reversed(ordered_coordinates):
	(x, y) =  ordered_coordinate
	cell = int(matrix[y][x])
	minimum_increment = 0
	has_right = x + 1 < len(matrix)
	has_down = y + 1 < len(matrix)
	if has_down and has_right:
		minimum_increment = min(int(minimum_paths_sums[y+1][x]), int(minimum_paths_sums[y][x+1]))
	elif has_down:
		minimum_increment = int(minimum_paths_sums[y+1][x])
	elif has_right:
		minimum_increment = int(minimum_paths_sums[y][x+1])
	minimum_paths_sums[y][x] = cell + minimum_increment

print minimum_paths_sums[0][0]
