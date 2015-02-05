digits = []
digsum = 0

for a in range(2,5*9**5):
    s = str(a)
    sum = 0
    for l in s:
        sum += int(l)**5
    if sum == a:
        digsum+=a
print(digsum)
