import math
piles = [30,11,23,4,20]
h = 5
piles = [3,6,7,11]
h = 8
# piles = [30,11,23,4,20]
# h = 6
piles = [2,2]
h = 2
piles = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h = 823855818
minimum = 1
maximum = max(piles)

while minimum <= maximum:
    mid = math.ceil(((maximum+minimum)/2))
    total = 0
    for i in range(len(piles)):
        total += math.ceil(piles[i]/mid)

    if total <= h:
        maximum = mid - 1
    else:
        minimum = mid + 1

print(minimum,maximum)
