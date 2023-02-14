nums = [-1,-2,-3,-4,3,2,1]
ans = 1
for i in range(len(nums)):
    ans = ans * nums[i]

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)