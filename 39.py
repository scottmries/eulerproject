import math

rs = dict()

for i in range(1,(1000)):
    for j in range(1,(1000)):
        k = math.sqrt(i*i+j*j)
        if math.floor(k)==k:
            p = i + j + k
            if p <= 1000:
                if p in rs:
                    rs[p] += 1
                else:
                    rs[p] = 1
print(rs)
mx,h = 0,0
for k in rs:
    v = rs[k]
    if v > mx:
        mx = v 
        h = k
print(h)
