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