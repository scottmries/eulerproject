# for cube with sides m, n, and p,
# the shortest path is the minimum of
# ((m + n)^2 + p^2 )^(1/2)
# ((m + p)^2 + n^2 )^(1/2)
# ((n + p)^2 + m^2 )^(1/2)

# given the winning length, 
# if its corresponding sides are two of a Pythagorean triple,
# it is a solution

# a recursive structure could be used to generate the cubes smaller than MxMxM
# from those those smaller than M-1xM-1xM-1