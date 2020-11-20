import math

M = 1
solutions = 0

squares = [True, True, False]

testDist = {1: {2: {}}}

try:
    print testDist[1][2][3]
except:
    print "nope"

def isSquare(s):
    return int(math.floor(math.sqrt(s)))**2 == s

while True:
    m = M
    for n in range(1, m + 1):
        for p in range(1, n + 1):
            least = (m + n)**2 + p**2
            if (m + p)**2 + n**2 < least:
                least = (m + p)**2 + n**2
            if (n + p)**2 + m**2 < least:
                least = (n + p)**2 + m**2
            if least > len(squares):
                for s in range(len(squares), least + 1):
                    squares.append(isSquare(s))
            if squares[least]:
                solutions += 1
    print "%s: %s" %(M, solutions)
    if M == 99 and solutions != 1975:
        print "solutions(99) != 1975"
        break
    if M == 100 and solutions != 2060:
        print "solutions(100) != 2060"
        break
    if solutions > 1000000:
        print "solution: %s" %(M)
        break
    M += 1