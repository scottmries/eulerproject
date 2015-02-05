sum = 0

for h in range(1,999999): 
    p = 1
    s = str(h) 
    bs = str(bin(h))[2:]
    for i, c in enumerate(s):
        if s[i] != s[len(s)-i-1]:
            p = 0
            break;
        else:
            for j, d in enumerate(bs):
                if bs[j] != bs[len(bs)-j-1]:
                    p = 0
                    break;
    if h%10000 == 0:
        print(h)
    if p==1:
        sum += h
        print(h)
print(sum)
