# starting with the final two columns,
# iterate over the first column's value,
# traverse the path between itself and all other values in the column,
# summing them,
# then adding the value adjacent to the right
# reduce the matrix's last two columns to this column's values
# if the matrix is one column, return its minimum

matrix_file = open('./data/p82.txt')
# matrix_file = open('./data/test.matrix')
matrix = list()
currentColumn = 0

for line in matrix_file:
	cells = line.split(',')
	row = list()
	for cell in cells:
		cell = cell.replace('\n','')
		row.append(int(cell))
	matrix.append(row)

def minimumCellSum(i, column1, column2):
	j = i
	min = column1[i] + column2[i]
	while j - 1 >= 0:
		j -= 1
		subcolumn = column1[j:i + 1]
		total = column2[j] + sum(subcolumn)
		if total < min:
			min = total
	j = i
	while j + 1 < len(column1):
		j += 1
		subcolumn = column1[i:j + 1]
		total = column2[j] + sum(subcolumn)
		if total < min:
			min = total
	return min

def reduceFinalTwoColumns(matrix):
	column2 = list()
	column = list()
	for i in range(len(matrix)):
		column2.append(matrix[i].pop())
		column.append(matrix[i].pop())
	newColumn = list()
	for i in range(len(column)):
		matrix[i].append(minimumCellSum(i, column, column2))
		newColumn.append(minimumCellSum(i, column, column2))
	print(newColumn)
	return matrix
	

def reduceMatrix(matrix):
	if len(matrix[0]) == 1:
		min = None
		for row in matrix:
			if min is None or row[0] < min:
				min = row[0]
		return min
	return reduceMatrix(reduceFinalTwoColumns(matrix))
	
print(reduceMatrix(matrix))