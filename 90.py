import itertools

# squares with 9s encoded as 6s
squares = ['01','04','06','16','25','36','46','64','81']

possible_sides = list(itertools.combinations([str(i) for i in range(0,10)],6))

print possible_sides

def flip_9(die):
	die = list(die)
	if '9' in die:
		die.remove('9')
		die.append('6')
	return list(die)

solution = 0

for die1 in possible_sides:
	for die2 in possible_sides:
		die1 = flip_9(die1)
		die2 = flip_9(die2)
		print die1, die2
		if int(''.join(die1)) >= int(''.join(die2)):
			possible_pairs = [side1 + side2 for side1 in die1 for side2 in die2] + [side2 + side1 for side1 in die1 for side2 in die2]
			if all(square in possible_pairs for square in squares):
				print die1, die2
				solution += 1

print solution
