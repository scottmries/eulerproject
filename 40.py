import math
c = ""
i = 1
p = 1
while len(c) < 1000000:
    for l in str(i):
        c += l
        if 10**int(math.log(len(c),10)+0.5) == len(c):
            p *= int(l)
    i += 1
print(p)
