# # find x s/t:
# # F(x) + F(x - 1) = F(P) + F(P - 1) + [2]
# # where F(n) is the list of factors of n
# # and where P > 10^12

# # note that 2x(x - 1) = P(P - 1)

# # 2x^2 - 2x = P^2 - P

# # what can be said about the factors of consecutive digits?
# # can they share any digits?
# # certainly they can't share a 2, because both would be even
# # in general, if n > 1, an and a2n will never be consecutive

# # F(15) = [3, 5]
# # F(14) = [2, 7]

# # they're disjoint

# # F(85) = [5, 17]
# # F(84) = [2, 2, 3, 7]

# # they're disjoint

# # what's the relation of R, the number of red discs, to x and P?

# # F(15) = [3, 5]
# # F(14) = [2, 7]
# # F(21) = [3, 7]
# # F(20) = [2, 5] + [2]

# # F(6) = [2, 3]


# # F(85) = [5, 17]
# # F(84) = [2, 2, 3, 7]
# # F(120) = [2, 2, 3, 5] + [2]
# # F(119) = [7, 17]

# # F(35) = [5, 7]

# # can P (or x) be derived from R?

# # x + R = P
# # x - 1 + R = P - 1
# # R = P - x (definition)

# # 2x(x - 1) = P(P - 1)
# # 2x(x - 1) = (x + R)(x + R - 1)
# # 2x^2 - 2x = x^2 + 2xR - x + R^2 - R
# # x^2 - x = 2xR + R^2 - R
# # x(x - 1) = R(R + 2x - 1)

# # x + R = P
# # x - 1 + R = P - 1

# # lower bound on (x - 1) is 1000000?
# # (x - 1)^2 = 10^12
# # but since x(x - 1) = 10^12 / 2,
# # the lower bound on x is 500000

# # F(500000) = [2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]
# # F(500001) = [3, ]
# # 166667

# # R can be derived from x:
# # 2x(x + 1) = P(P + 1)
# # x + R = P

# # given x, double it, and multiply that by x + 1
# # subtract x from this quantity to get R
# # R will be much more manageable to factor

# # given R, is it possible to derive x?

# # x + R = P
# # 2x(x - 1) = P(P - 1)
# # 2x^2 - 2x = P^2 - P
# # 0 = P^2 - P - (2x^2 - 2x)
# # P = (1 +/- rad(1 + 4(2x^2 - 2x))) / 2
# # P = (1 +/- rad(1 + 8x(x - 1))) / 2

# # R = (1 +/- rad(1 + 8x(x - 1))) / 2 - x
# # 1 + 8x(x - 1) is a square, since R must be an integer
# # rad(1 + 8x(x - 1)) is odd, since R must be an integer
# # s = 1 + 8x(x - 1)
# # 0 = 8x^2 - 8x + (1 - s)
# # x = (8 +/- rad(64 - 32(1 - s))) / 16

# # 64 - 32 + 32s = 32 + 32s = 32(s + 1) must be a square
# # 32(s + 1) must be a square! since x must be an integer

# # s is a square
# # 32(s + 1) is also a square

# from collections import defaultdict
from math import ceil, floor, sqrt

def int_square_root(s):
    return floor(sqrt(s))

def is_square(s):
    return pow(int_square_root(s), 2) == s

# def sieve(limit):
#     primes = [i for i in range(0, limit)]
#     i = 2
#     while i < len(primes):
#         value = primes[i]
#         if value == 'x':
#             i += 1
#         else:
#             if value > sqrt(limit):
#                 break
#             factor = 2
#             composite = value * factor
#             while composite < limit:
#                 primes[composite] = 'x'
#                 factor += 1
#                 composite = value * factor
#             i += 1
#     return [prime for prime in primes if prime != 'x' and prime != 0 and prime != 1]


# # primes = sieve(1000)

# # def check(x):
# #     factors = factor_set(x) + factor_set(x - 1) + [2]
# #     factors.sort()
# #     factors_product = 1
# #     for factor in factors:
# #         factors_product *= factor
# #     P = int_square_root(factors_product) + 1
# #     print(f'P: {P}')
# #     print(f'factors: {factors}')
# #     return P * (P - 1) == factors_product

# # def factor_set(x):
# #     factors = defaultdict(lambda: 0)
# #     while x > 1:
# #         for prime in primes:
# #             if x % prime == 0:
# #                 factors[prime] += 1
# #                 x //= prime
# #     return factors

# # this is essentially brute force, and won't be fast enough
# # S(S - 1) will have a factor of 2, since either x or x - 1 will be even, 
# # and another factor of 2 since it's twice x(x - 1)

# # the set F of factors of x and x - 1 is the same set S + [2]
# # can this set be constructed somehow?

# # given some candidate N, the factorization of N can be expressed as
# # x[0], x[1], ... x[n]
# # where x[0] corresponds to the number of factors of 2 in N, x[1] number of 3s, 
# # up to x[n], the number of factors of the highest prime >= sqrt(N)

# # given some x, find the factors of x and x - 1 in the above form
# # appending a 2, S and S - 1 can only have distinct factor sets whose products differ by one


# # print(factor_set(140))
# # print(factor_set(pow(10, 12)))

# # limit = pow(10, 12)
# limit = pow(10, 7)
# # limit = pow(10, 6)
# # limit = pow(10, 5)
# # limit = pow(10, 3)
# primes = sieve(limit)

# print(primes[-1])
# print(len(primes))

# factorizations = defaultdict(lambda: defaultdict(lambda: 0))

# def factors_of_x_and_neighbor(x):
#     factors = dict(factorizations[x])
#     factors.update(dict(factorizations[x - 1]))
#     return {k: v for k, v in sorted(factors.items(), key=lambda item: item[0])}

# def find_solutions(limit):
#     # naive, brute-force solution
#     for root in range(1, limit):
#         s = root * root
#         if(is_square(32 * (s + 1))):
#             # x = (8 +/- rad(64 - 32(1 - s))) / 16
#             # always negative when s is a positive integer
#             # low_x = (8 - int_square_root(32 * (s + 1))) / 16
#             x = (8 + int_square_root(32 * (s + 1))) // 16
#             print(f'x: {x}')
#             print(f'factors: {factors_of_x_and_neighbor(x)}')
#             # print(f'check x: {check(x)}')

# for prime in primes:
#     print(prime)
#     i = 1
#     p = 1
#     power = pow(prime, p)
#     while power < limit:
#         while power * i < limit:
#             factorizations[power * i][prime] += 1
#             i += 1
#         i = 1
#         p += 1
#         power = pow(prime, p)



# # print(prime * i)
# # print(factorizations[prime * i])

# # print(factorizations[limit - 1])

# print(find_solutions(limit))

# # print(factorizations)

# # for i in range(1, 1000000):
# #     if i % 1000000 == 0:
# #         print(factorizations[i])

# # print(factorizations[limit - 1])

# # i = pow(10, 12)
# # i = 1
# # factorizations[i] = factor_set(i)

# # def find_x(factor_set):

# # while True:
# #     i += 1
# #     factorizations[i] = factor_set(i)
# #     factors = factorizations[i - 1] + factorizations[i]
# #     if find_x(factors):
# #         print(i)
# #         break

# # solution? 493
# # (493/697)(492/696)
# # yes

# # found = False
# # i = pow(10, 12)
# # while found is False:

# # start from pow(10, 12) as S
# # candidate for x(x - 1) is S(S - 1)/2
# # given S, what's x? and given x, what's R? can we iterate on R?
# # x^2 - x = (S^2 - S)/2
# # x^2 - x - ((S^2 - S)/2) = 0
# # x^2 - x + ((S - S^2) / 2) = 0
# # x = (1 +/- rad(1 - 4((S - S^2) / 2))) / 2
# # x = (1 +/- rad(1 - 2(S - S^2))) / 2
# # x = (1 +/- rad(1 + 2S^2 - 2S)) / 2

# # 2S^2 - 2S + 1 must be some n^2
# # n = rad(2)S - rad(2)rad(S) + 1
# # S is a square!

# limit = pow(10, 12)

# by definition 2x(x - 1) = s(s - 1) for x, s in Naturals
# 2x^2 - 2x - (s^2 - s) = 0
# (2 +/- rad(4 + 8(s^2 - s))) / 4
# 4 + 8(s^2 - s) is a square, and its root even
# this holds for 21 and 120

# for some r, if r^2 = (n^2 - 64) / 2 for n, r in Naturals
# S = (8 +/- rad(64 - 32(4 - n^2))) / 16

# for i in range(1, 1000):
#     if is_square((i * i * 2) + 64):
#         n = int_square_root((i * i * 2) + 64)
#         print(n)
#         print (8 + pow(64 - 32 * (4 - pow(n, 2)), 1/2) / 16)
#         print (8 - pow(64 - 32 * (4 - pow(n, 2)), 1/2) / 16)

base = pow(10, 11)
index = 1
while True:
    q = pow(base, 2)
    print(f'index: {index}, q: {q}')
    # if(is_square(8 * q - 4)):
    #     p = int((2 + pow((8 * q - 4), 1/2))/4)
    #     print(f'p: {p}')
    #     if(p > pow(10, 12)):
    #         print(f'solution (p): {p}')
    #         break
    base += 1
    index += 1
