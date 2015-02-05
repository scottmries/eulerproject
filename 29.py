distinct = []
for a in range(2,101):
    print(a)
    for b in range(2,101):
        if a**b not in distinct:
            distinct.append(a**b)
print(len(distinct))
