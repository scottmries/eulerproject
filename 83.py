# the rules are as simple as this:
# if a square is adjacent to the least end-square,
# its direction points to that end-square, 
# and that end-square's value gets added to it and it becomes an end-square itself
# if a square's minimal neighbor plus itself plus the least end-square is greater than
# its minimal adjacent end-square,
# its minimal path is toward its minimal adjacent end-square (and can be resolved)
# if all of an end-square's neighbors are end-squares or "dead",
# it can be considered dead, and no longer considered at all
# when a single square remains, its value is the minimal sum.
# the optimal way to check squares is looping over the live, non-end neighbors of end-squares,
# the first of which is the bottom right corner

class Square:
    def __init__(self, coordinates, value):
        self.coordinates = coordinates
        self.initial_value = value
        self.end_value = None

    def end(self, addend):
        self.end_value = self.initial_value + addend

    def set_neighbors(self):
        global matrix
        (y, x) = self.coordinates
        self.neighbors = list()
        if x + 1 < len(matrix):
            neighbor = matrix[x + 1][y]
            if neighbor.end_value is None:
                self.neighbors.append(neighbor)
        if x - 1 >= 0:
            neighbor = matrix[x - 1][y]
            if neighbor.end_value is None:
                self.neighbors.append(neighbor)
        if y + 1 < len(matrix[0]):
            neighbor = matrix[x][y + 1]
            if neighbor.end_value is None:
                self.neighbors.append(neighbor)
        if y - 1 >= 0:
            neighbor = matrix[x][y - 1]
            if neighbor.end_value is None:
                self.neighbors.append(neighbor)
    
    def end_neighbors(self):
        self.set_neighbors()
        for neighbor in self.neighbors:
            neighbor.end(self.end_value)
        

matrix_file = open('./data/p83.txt')
# matrix_file = open('./data/test.matrix')

matrix = list()

column = 0
for line in matrix_file:
    cells = line.split(',')
    row = list()
    for row_index in range(len(cells)):
        cell = cells[row_index].replace('\n','')
        row.append(Square((row_index, column), int(cell)))
    column += 1
    matrix.append(row)

bottom_right = matrix[-1][-1]
bottom_right.end(0)

top_left = matrix[0][0]

endSquares = [bottom_right]

while True:
    least_square = None
    least_value = None
    least_square_index = None
    print('end squares')
    for square_index in range(len(endSquares)):
        print(endSquares[square_index].coordinates)
        square = endSquares[square_index]
        if least_value is None or square.end_value < least_value:
            least_value = square.end_value
            least_square = square
            least_square_index = square_index
    print("least square")
    print("%s: %s" %(least_square.coordinates, least_square.end_value))
    least_square.end_neighbors()
    print("least square neighbors")
    for neighbor in least_square.neighbors:
        print(neighbor.coordinates)
    endSquares += least_square.neighbors
    del endSquares[least_square_index]
    if top_left in least_square.neighbors:
        solution = top_left.end_value
        break

print(solution)
        

