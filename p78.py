import math

# p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7)
# sum for k = 1 k < infinity of (n - pentagonal(k)) * (-1) ** (math.floor((k - 1) / 2))

partitionsOfN = [1, 1]

def pentagonal(n):
    return  n * (3 * n - 1) / 2

def p(n):
    sum = 0
    k = 1
    power = 1
    while n - pentagonal(k) >= 0:
        sum += partitionsOfN[n - pentagonal(k)] * (-1) ** (math.floor((power - 1) / 2))
        if k > 0:
            k = -k
        else:
            k = -k + 1
        power += 1
    sum = int(sum % 1000000)
    partitionsOfN.append(sum)
    return sum

n = 2
while p(n) != 0:
    print("n: %s, p(n): %s" %(n, partitionsOfN[n]))
    if n == 5 and partitionsOfN[5] != 7:
        raise Exception('Test case is false')
    n += 1

print("solution:")
print("%s: %s" %(n, partitionsOfN[n]))
