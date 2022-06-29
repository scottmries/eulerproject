# ¯\_(ツ)_/¯

# i
# b, r, d => F(b), F(r), F(d)
# b - 1, r, d - 1 => F(b - 1), F(r), F(d - 1)

# 1
# 15, 6, 21 => (3, 5), (2, 3), (3, 7)
# 14, 4, 20 => (2, 7), (2, 3), (2, 5)

# 2
# 85, 35, 120 => (5, 17), (5, 7), (5, 24)
# 84, 35, 119 => (12, 7), (5, 7), (17, 7)

# NB that F(r2) is the XOR of F(b - 1) and F(d - 1)

# 3
# 493, 204, 697 => (17, 29), (17, 12), (17, 41)
# 492, 204, 696 => (41, 12), (17, 12), (58, 12)

# NB that F(r3) is the XOR of F(b - 2) and F(d - 2)

# 4 
# 2871, 1189, 4060 => (99, 29), (41, 29), (140, 29)
# 2870, 1189, 4059 => (41, 70), (41, 29), (41, 99)

# and again...

# 5
#  => (99, ), (99, 140), (99, )
#  => ( , 140), (99, 140), (, 140)

# a = 99
# b = 140
# r = a * b

# 2 * (99 * x) (99 * (x - 1)) = (99 * y) (99 * (y - 1))

# 2a^2x(x-1) = a^2y(y - 1)
# x + r = y

# 2a^2x(x - 1)

# Given r1 and F(r1), 6 and [2, 3], derive b1.
# Find F(b1) by finding which of F(r1) divides b1, call it f1, and the other f2. f3 is b1 / f1.
# d1 is then (f2 + f3) * f1, and f4 is f2 + f3.
# f5 = (b1 - 1) / f2, and f6 = (d1 - 1) / f2

# There are now six factors. 
# Discard f1 and f2. 
# Two of the remaining factors are the same; discard one.
# One remaining factor is twice another; discard it.
# The remaining factors are f`m and f`n, and F(r2) is then [f`m, f`n].

from math import floor, sqrt


def getNextSolution(r, Fr):
    b = (1 + 2 * r + floor(sqrt(8 * r * r + 1))) // 2
    if b % Fr[0] == 0:
        [f1, f2] = Fr
    else:
        [f2, f1] = Fr
    f3 = b // f1
    f4 = f2 + f3
    d = f4 * f1
    f5 = (b - 1) // f2
    f6 = (d - 1) // f2
    factors = [f1, f2, f3, f4, f5, f6]
    Fr = list(set([i for i in factors if (i / 2 not in factors) and i != f1 and i != f2]))
    r = Fr[0] * Fr[1]
    return [b, r, Fr, d]

r = 6
Fr = [2, 3]

while True:
    solution = getNextSolution(r, Fr)
    [b, r, Fr, d] = solution
    print(b, d)
    if d > pow(10, 12):
        break
print(b)