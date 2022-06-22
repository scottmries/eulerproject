from data96data import lines
import copy, math

boards = []
for i, line in enumerate(lines):
    if(i % 10 == 0):
        board = []
    else:
        board.append([int(digit) for digit in line])
    if(i % 10 == 9):
        boards.append(board)

def cells_in_row(_, y, board):
    return [cell for cell in board[y]]

def cells_in_column(x, _, board):
    return [row[x] for row in board]

def cells_in_box(x, y, board):
    xs = [cell + (x // 3) * 3 for cell in range(0, 3)]
    ys = [cell + (y // 3) * 3 for cell in range(0, 3)]
    cells = []
    for x_cell in xs:
        for y_cell in ys:
            cells.append(board[y_cell][x_cell])
    return cells

def seen_cells(x, y, board):
    return cells_in_row(x, y, board) + cells_in_column(x, y, board) + cells_in_box(x, y, board)

def valid_digit(value):
    return isinstance(value, int) and value != 0

def seen_digits(x, y, board):
    return set(cell for cell in seen_cells(x, y, board) if valid_digit(cell))

def available_digits(x, y, board):
    digits = list(set(i for i in range(1, 10)) - seen_digits(x, y, board))
    if(len(digits) == 1):
        return digits[0]
    return digits

def print_board(board):
    for row in board:
        print(row)

def resolve_coordinate(x, y, board):
    value = board[y][x]
    if(not valid_digit(value)):
        candidates = available_digits(x, y, board)
        if(isinstance(candidates, int)):
            board[y][x] = candidates
        else:
            if(len(candidates) > 0):
                board[y][x] = available_digits(x, y, board)
            else:
                return False
    return board

def resolved_digits(board):
    count = 0
    for x in range(0, 9):
        for y in range(0, 9):
            value = board[y][x]
            if(valid_digit(value)):
                count += 1
    return count

def board_solved(board):
    return resolved_digits(board) == 81

def least_candidates_cell(board):
    least_candidates = [i for i in range(1, 10)]
    coordinates = [None, None]
    for col_index, y in enumerate(board):
        for row_index, x in enumerate(y):
            if isinstance(x, list):
                if len(x) == 2:
                    return [row_index, col_index]
                elif len(x) < len(least_candidates):
                    least_candidates = x
                    coordinates = [row_index, col_index]
    return coordinates

def guess(index, board):
    print(f'guessing on board {index}')
    [x, y] = least_candidates_cell(board)
    candidates = board[y][x]
    for candidate in candidates:
        guess_board = copy.deepcopy(board)
        guess_board[y][x] = candidate
        guess_solution = solve(index, guess_board)
        if(guess_solution):
            return guess_solution

def solve(index, board):
    last_resolved_digits = 0
    while(not board_solved(board)):
        for y in range(0, 9):
            for x in range(0, 9):
                cell = resolve_coordinate(x, y, board)
                if cell == False:
                    return False
                else:
                    board = resolve_coordinate(x, y, board)
        if resolved_digits(board) == last_resolved_digits:
            print(f'cannot solve board {index}')
            board = guess(index, board)
            return board
        if(board_solved(board)):
            print(f'solved board {index}')
            return board
        last_resolved_digits = resolved_digits(board)

def digits_from_solved_board(board):
    return int(str(board[0][0]) + str(board[0][1]) + str(board[0][2]))

solution = 0

# boards = [boards[0]]
for index, board in enumerate(boards):
    solved_board = solve(index, board)
    if solved_board != False:
        solution += digits_from_solved_board(solved_board)
    # write a function solve() that
    # tries the solve
    # if it works, output solve's value
    # if not,
    # find the cell with the fewest possibilities
    # "guess" each value by resolving it into a new board
    # then passing it back into solve

print(solution)