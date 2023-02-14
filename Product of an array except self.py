nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
# nums = [0,0,0,0]
nums = [1,0]
nums = [0,4,0]
flag = False
if 0 in nums:
    flag = True
ans = []
product = 1
count = 0
for i in range(len(nums)):
    if nums[i] == 0:
        count += 1
if count == len(nums):
    print(nums)
if flag == False:
    for i in range(1,len(nums)):
        product = product * nums[i]
    ans.append(product)
    for j in range(1,len(nums)):
        ans.append(product//nums[j])
else:
    for i in range(len(nums)):
        if nums[i] != 0:
            product = product * nums[i]
    for j in range(len(nums)):
        if nums[j] != 0:
            ans.append(0)
        else:
            ans.append(product)


