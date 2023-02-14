nums = [1,3]
# nums = [5,1,6]
nums = [3,4,5,6,7,8]
sum = 0
f = nums[0]
for i in range(len(nums)):
    sum += nums[i]
    y = nums[i]
    for j in range(i+1,len(nums)):
        x = 0
        x = nums[i]^nums[j]
        sum += x
        y = y^nums[j]
    sum += y
print(sum)