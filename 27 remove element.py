nums = [0,1,2,2,3,0,4,2]
val = 2
for i in range (len(nums)):
    if val in nums:
       nums.remove(val)
print(nums)