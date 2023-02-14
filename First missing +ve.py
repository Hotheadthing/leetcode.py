nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
# nums = [1]
nMap = {}

for i in range(len(nums)):
    if nums[i] > 0 and nums[i] not in nMap:
        nMap.__setitem__(nums[i],1)
arr = []
for i in range(len(nums)):
    if i+1 not in nMap:
        arr.append(i+1)
        break

if arr == []:
    print(nums[-1]+1)
else:
    print(arr[0])