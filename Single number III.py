nums = [1,3,4,2,2]
x = nums[0]

for i in range(1,len(nums)):
    x = x^nums[i]
    print(x)