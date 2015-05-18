limit = 1500000

solution = 0

wirelengths = list()
for i in xrange(0, limit+1):
    wirelengths.append([])

coprime_pairs = list()


def farey(n, asc=True):
    """Print the nth Farey sequence, either ascending or descending."""
    if asc:
        a, b, c, d = 0, 1,  1, n     # (*)
    else:
        a, b, c, d = 1, 1, n-1, n     # (*)
    print "%d/%d" % (a, b)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        # print a, b
        if a < b:
            coprime_pairs.append((a, b))
            print "%d/%d" % (a, b)

# m**2 + n**2 + m**2 - n **2 + 2*m*n <= limit
# 2*m**2 + 2*m*n <= limit
# m**2 + m*n <= limit/2
# m + n <= limit/(2*m)

# given this, the square root of the limit is sufficiently large

farey(int(limit**0.5))

for coprime_pair in coprime_pairs:
    m = coprime_pair[1]
    n = coprime_pair[0]
    k = 1
    while True:
        a = k*(m**2 + n ** 2)
        b = k*(2*m*n)
        c = k*(m**2 - n ** 2)
        wirelength = a + b + c
        if wirelength <= limit:
            triple = [a, b, c]
            triple.sort()
            if triple not in wirelengths[wirelength]:
                wirelengths[wirelength].append(triple)
            k += 1
        else:
            break

for wirelength in wirelengths:
    if len(wirelength) == 1:
        solution += 1
    print e, wirelength

print solution
