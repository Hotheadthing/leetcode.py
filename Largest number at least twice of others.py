nums = [3,6,1,0]
# nums = [1,2,3,4]
nums = [0,0,0,1]
comp = max(nums)
ans = 1
for i in range(len(nums)):
    if nums[i] != comp:
        if nums[i] * 2 > comp:
            ans = -1
            break
if ans == -1:
    print(-1)
else:
    print(nums.index(comp))