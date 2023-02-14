nums = [1,2,2,4]
nums = [1,1]
nMap = {}
ans = []
zero = 0
two = 0
for i in range(len(nums)):
    nMap.__setitem__(i+1,0)

for i in range(len(nums)):
    nMap[nums[i]] += 1

for d in nMap:
    if nMap[d] == 2:
        two = d
    if nMap[d] == 0:
        zero = d
ans.append(two)
ans.append(zero)

print(ans)