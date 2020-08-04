# -*- coding: UTF-8 -*-

# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

# For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

# Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

# In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

# What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

# One strategy would be to iterate over 2->12000, finding every lowest PS number,
# but there may be a way to anticipate redundant PS numbers ahead of time?

import numpy

maximumK = 100

smallestProductSumsOfSize = {2: 2, 3: 6, 4: 8, 5: 8, 6: 12}

possibleProductSumSets = {1: []}
for i in range(1, 10):
    possibleProductSumSets[1].append({
        'set': [i],
        'product': i,
        'sum': i
    })

def getSmallestProductSumOfSize(k):
    minimumPSNumber = None
    set = None
    for s in possibleProductSumSets[k]:
        if s['product'] == s['sum']:
            if s['product'] < minimumPSNumber or minimumPSNumber is None:
                minimumPSNumber = s['product']
                set = s['set']
    return {'value': minimumPSNumber, 'set': set}

def getNextSetOfDigits(sets):
    nextSet = []
    for s in sets:
        lastValue = s['set'][-1]
        for i in range(lastValue, 10):
            # since these sets will be in ascending order,
            copy = s['set'][:]
            copy.append(i)
            product = i * s['product']
            sum = i + s['sum']
            # if the set's product exceeds the set's sum,
            # it will always exceed the set's sum;
            # it's therefore not a possibility
            # this condition is key:

            # assume the rest of the digits are additively minimized by choosing i,
            # does the product exceed the sum?
            if product <= sum and product * i <= maximumK * 9:
                # print(copy)
                # print len(copy)
                # print 'product', product
                # print 'sum', sum
                nextSet.append({
                    'set': copy,
                    'product': product,
                    'sum': sum
                })
    return nextSet

last = 0
sum = 0
values = []
for i in range(2, maximumK):
    possibleProductSumSets[i] = getNextSetOfDigits(possibleProductSumSets[i - 1])
    print possibleProductSumSets[i]
    smallest = getSmallestProductSumOfSize(i)
    print i, smallest['value']
    set = None
    if smallest['value'] > last:
        sum += smallest['value']
        last = smallest['value']
        set = smallest['set']
    if last not in values:
        values.append(last)
    # print i, set
print numpy.sum(values)
print values
