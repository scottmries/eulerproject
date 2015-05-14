# The string xyz means: there is an x, and somewhere after that, there is a y, and somewhere after that there is a z
# With strings xyz and xab, [y,z,a,b] in some order, come after x
# Wtih strings xyz, xab, and xya, we know that y comes before a and after
# x, that a comes before b and after x, and that z comes somewhere after a

# Maybe it makes sense to find the first digit first, and then move on from there?
# The first digit could be 3,6,1,7,2,or,8
# Does 3 appear after 6,1,7,2,or 8 etc.

# is the trick here to sort these by afterness?

numbers_that_come = dict()
for i in xrange(0, 10):
    numbers_that_come[str(i)] = {'before': set(), 'after': set()}
passcodes = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729,
             729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]
passcodes = list(set(passcodes))

print passcodes

for passcode in passcodes:
    for position, digit in enumerate(str(passcode)):
        print passcode
        for earlier_digit in [earlier_digit for e, earlier_digit in enumerate(str(passcode)) if e < position]:
            numbers_that_come[digit]['before'].add(earlier_digit)
        for earlier_digit in [earlier_digit for e, earlier_digit in enumerate(str(passcode)) if e > position]:
            numbers_that_come[digit]['after'].add(earlier_digit)
for key, value in numbers_that_come.items():
    for position, numbers in value.items():
        print key, position, numbers

# with the printed information, the manual work is simple:
    # 73162890
