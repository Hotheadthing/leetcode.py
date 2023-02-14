nums = [3,2,3,2,2,2]
nums = [1,2,3,4]
nMap ={}

for i in range(len(nums)):
    if nums[i] not in nMap:
        nMap.__setitem__(nums[i],1)
    else:
        nMap[nums[i]] += 1

flag = True

for d in nMap:
    if nMap[d] % 2 != 0:
        flag = False
        break

print(flag)