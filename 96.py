import math

puzzles_file = open('./data/p96.txt')
puzzles = list()
for line in puzzles_file:
    if "Grid" in line:
        if "01" not in line:
            puzzles.append(puzzle)
        puzzle = list()
    else:
        puzzle.append([int(char) for char in line[0:-1]])

print([[] for _ in range(9)])

def getCellsGroupsCoordinates(x, y):
    row = [(i, y) for i in range(9)]
    column = [(x, i) for i in range(9)]
    xFloor = int(math.floor(x / 3) * 3)
    yFloor = int(math.floor(y / 3) * 3)
    square = [(i, j) for i in range(xFloor, xFloor + 3) for j in range(yFloor, yFloor + 3)]
    return { "row": row, "column": column, "square": square }

print(getCellsGroupsCoordinates(4, 5))
# for puzzle in puzzles:
