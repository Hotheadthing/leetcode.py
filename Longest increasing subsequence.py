nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
count = 1
ans = 0
for i in range(len(nums)):
    x = nums[i]
    for j in range(i+1,len(nums)):
        if nums[j] > x:
            count += 1
            x = nums[j]
    ans = max(ans,count)
    count = 1

print(ans)