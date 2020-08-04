# starting in the bottom right corner,
# every cycle, enlarge a triangle of allowed moves
# finding the minimal path for each with its allowable moves
# the squares on this triangle's outer edge are all the same number of moves from the bottom right corner
# do this from bottom right to top left, then top left to bottom right, then bottom right to top left again
# possibly one more cycle? possibly 79 more cycles?
# this should give each square complete knowledge of the optimal move away from it?
# then just follow that path