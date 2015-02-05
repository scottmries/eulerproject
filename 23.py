import math
abuns, summables,  nsum = [], [""]*28123, 0
for i in range(1,28124):
    sum = 0
    for j in range(1,math.floor(math.sqrt(i))+1):
        if i%j==0:
            sum += j
            if j > 1 and j != math.sqrt(i):
                sum+= i/j
    if sum > i:
        abuns.append(i)
for i in abuns:
    for j in abuns:
        if i+j < 28124:
            summables[i+j-1] = "Yes"
for e,i in enumerate(summables):
    if i == "":
        nsum += e + 1
print(nsum)
