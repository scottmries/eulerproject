# the bottom right corner is the end, there's no choice to make.
# reaching a square directly adjacent to the bottom right corner, x,
# no choice but going to the end, y, is optimal, since some k + x + y > x + y.
# reaching a square adjacent to x, there are at least two choices:
# go to x,
# or go directly around x, whichever is minimal.

# this obviously needs to be solved on a per-square-basis,
# with each square's sub-solution having its minimum and a single direction

# squares along the right edge's optimal direction can never be up,
# since being able to reach that square, 
# then move up from it,
# then get back to the bottom right would not be possible without the path re-crossing itself,
# and hence using a square multiple times, suboptimally

# if a square's optimal direction is found to point to an adjacent square with a known minimum value,
# resolve the initial square's value to its initial value plus that of the adjacent square
# if not, mark the optimal direction of the change but do not change its value

# squares will have these values:
# value, which will change to the minimum value of its remaining path if one is found
# whether one has been found (a Boolean)
# the optimal direction
# whether this square is an end square


# once all of a solved square's neighbors are solved and its total add to theirs,
# it can be removed

# once a solved square's adjacent square in its optimal direction is solved,
# its direction no longer matters,
# and it becomes like an end in itself

# THIS IS THE GENERAL RULE:
# for any given square, 
# if that square is adjacent to an "end" square,
# and that end-square is the least of the end square,
# its optimal direction is toward that square.
# if the minimal end-square is not adjacent,
# but the least adjacent square (solved or not) plus that least end-square is more than the lease end-square,
# then the direction is toward the least adjacent end-square
# otherwise it remains unknown

# after every round of adding squares, (or, differently checking squares exactly one square further away from the end)
# test whether new directions, minima, solutions, or end squares have been found
# if so, check again, until no more have been found,
# then add another round of adjacent squares, (or, differently check again from the squares nearest the endpoint)

# if an unsolved square has an adjacent square whose minimal direction points to it,
# the unsolved square's minimal direction will not be toward that square,
# as that square would just lead back to it

# if, by following a square's minimal direction along the minimal directions of the next square's path,
# we reach an end-square, that square is solved

# the bottom-left corner's optimal direction will always be right,
# the top-right corner's will always be down

# a top edge square's optimal direction cannot be left
# a left edge square's optimal direction cannot be up
# since neither would be able to reach the end without doubling back

# since some square will always be adjacent to the minimal end-square,
# a solveable square will always be present

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