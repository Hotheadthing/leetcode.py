nums = [3,10,5,25,2,8]
index0 = []
index1 = []
m, mask = 0, 0

for i in range(32)[::-1]:
    mask |= 1 << i
    prefixes = {n & mask for n in nums}
    print(prefixes)
    tmp = m | (1 << i)
    print(tmp)
    #
    # if any(prefix ^ tmp in prefixes for prefix in prefixes):
    #     m = tmp

print(m)