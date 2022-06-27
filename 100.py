from math import ceil, floor, sqrt

# Where b is the number of blue discs, r the red, and d the total, b, r, and d in N
# 2b(b - 1) = d(d - 1) and b + r = d by definition.
# Consider the areas D = d(d - 1), B = b(b - 1), and R = D - B
# R = d(d - 1) - b(b - 1) => R = 2b(b - 1) - b(b - 1) = b(b - 1)
# Assume b is given.
# d^2 - d - b^2 + b = b^2  - b => d^2 - d + (2b - 2b^2) = 0 = d^2 - d + 2b(1 - b)
# By the quadratic formula
# d = (1 +/- sqrt(8b^2 - 8b + 1))/2
# which implies that 8b^2 - 8b + 1 is a perfect square, 
# since if it were not, its square root would be irrational, and the rational operations that apply to it to reach d would not produce a rational d, and therefore not a natural d
# this is borne out empirically from the given solutions:

def is_square(n):
    return pow(int(sqrt(n)), 2) == n

def is_almost_square(n):
    root = sqrt(n)
    return ceil(root) * floor(root) == n

def form_of_b(b):
    return 8 * pow(b, 2) - 8 * b + 1

assert is_square(form_of_b(15))
assert is_square(form_of_b(85))

almost_squares = [0, 1]
def backfill_almost_squares_to(n):
    next_almost_square = len(almost_squares) * (len(almost_squares) - 1)
    while next_almost_square < n:
        almost_squares.append(next_almost_square)
        next_almost_square = len(almost_squares) * (len(almost_squares) - 1)
    return next_almost_square == n

# for some square s, s = 8b^2 - 8b + 1 => (s - 1)/8 = b(b - 1)
# b(b - 1) is the form of an "almost square" number, which is twice a triangle number
# the nth triangle number, Tn, is 2n(n - 1)

# r is the square root of s

# (r^2 - 1)/8 = b(b - 1)
# (r + 1)(r - 1) = 8b(b - 1)
# C = (r + 1)(r - 1)
# 8b^2 - 8b - C

# 8 * 15 * 14 = 1680
# t = 21

# 40 * 42

# (int(sqrt(8b(b - 1))) + 1)(int(sqrt(8b(b - 1))) - 1)

# 8 * 85 * 84 = 57120
# t = 120

# 238 * 240

# t(t - 1) = 2 * b(b - 1)

# factors of Tn?

# 0 => 0 => [0, 1]
# 1 => 1 => [1, 1]
# 2 => 3 => [1, 3]
# 3 => 6 => [2, 3]
# 4 => 10 => [2, 5]
# 5 => 15 => [3, 5]
# 6 => 21 => [3, 7]
# 7 => 28 => [4, 7]
# 8 => 36 => [4, 9]
# 45 => [5, 9]
# 55 => [5, 11]
# 66 => [6, 11]
# 78 => [6, 13]
# 91 => [7, 13]
# 105 => [7, 15]
# 120 => [8, 15]

triangles = []

def binary_search(needle, haystack):
    if len(haystack) == 0:
        return False
    if len(haystack) == 1:
        if needle == haystack[0]['triangle']:
            return haystack[0]
        return False
    if needle >= haystack[len(haystack) // 2]['triangle']:
        return binary_search(needle, haystack[(len(haystack) // 2):])
    return binary_search(needle, haystack[:(len(haystack) // 2)])

i = 0
triangles = []
while True:
    odd_factor = i
    if i % 2 == 0:
        odd_factor = i + 1
        other_factor = i // 2
    else:
        odd_factor = i
        other_factor = (i - 1) // 2 + 1
    Ti = odd_factor * other_factor
    triangles.append(Ti)
    # n = floor(sqrt(2 * Tn))
    j = floor(sqrt(Ti))
    Tj = triangles[j]
    # print(f'triangle: {Ti}')
    if Ti == 2 * Tj:
        discs = i + 1
        blue_discs = j + 1
        red_discs = discs - blue_discs
        print(f'discs: {discs}. blue discs: {blue_discs}. red discs: {red_discs}')
    if(i + 1 > pow(10, 5)):
        # print(triangles)
        exit()
    i += 1
# I think there is a ripping fast way to do this from this algorithm

# t(t - 1) is twice some triangle number which is also twice some other triangle number, b(b - 1)

# 210 = [2, 3, 5, 7]
# since right-hand is even, r must be odd
# if F(x) returns an array of factors of x,
# since r - 1 is even,
# F(r - 1) + [2] = F(r + 1) (NOT THE CASE!)

# [4][6] => F(4) = [2, 2] => F(6) = [2, 3]

# [16][18] => F(16) = [2, 2, 2, 2] => [2, 3, 3]

# [32][34] => F(32) = [2, 2, 2, 2, 2] => [2, 17]

# [28][30] => F(28) = [2, 2, 7, 7] => [2, 3, (5)]

# [24][26]

# [36][38] => F(36) = [2, 2, 3, 3] =>

# r has f factors of 2

# [100][102] => F(100) = [2, 2] + [...] => [2, 3] + [...]

# since 2b(b - 1) = d(d - 1) and 10^12 < d
# 10^24 < 2(b - 1)(b - 1) => 5 * 10^12 + 1 < b
# 8 * (5 * 10^12 + 1) ^ 2 - 8 * (5 * 10^12 + 1) + 1 < s
# 8 * 5 * 10^12 + 1 (5 * 10^12) < s
# the lower bound for the square root of s, r, is 5 * 10^12

# call the lower bound for r 10^12

# x is almost square if floor(sqrt(x))ceil(sqrt(x)) = x
# for some square s, determine if (s - 1)/8 is almost-square

# triangles = [0, 1]
# almostSquares = [-1, 0]

# for i in range(2, pow(10, 12)):
#     triangle = triangles[-1] + i
#     triangles.append(triangle)
#     almostSquare = i * (i - 1)
#     print(f'triangle: {triangle}, i: {i}, ratio: {triangle / i}')
#     print(f'almost square: {almostSquare}, i: {i}, ratio: {almostSquare / i}')

# print(triangles[-1])

# r = pow(10, 12)
# while True:
#     candidate = (pow(r, 2) - 1) / 8
#     print(candidate)
#     if(is_almost_square(candidate)):
#         print(ceil(sqrt(candidate)))
#         # break
#     r += 1

# assert backfill_almost_squares_to(15 * 14)

# r = pow(10, 12)

# while True:
#     candidate = (r + 1) * (r - 1) / 8
#     if backfill_almost_squares_to(candidate):
#         b = ceil(sqrt(candidate))
#         print(b)
#         if b > 10^12:
#             print(b)
#     r += 1