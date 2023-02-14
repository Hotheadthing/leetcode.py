nums = [1,1,1,1,1,1,1,1]
# nums = [1,4,4]
nums1 =[]
target = 11
count = 0
answer = 0
flag = 0
nums.sort()
if target in nums:
    count = 1
    flag = 1
if flag == 0:
    for i in range(len(nums) - 1, -1, -1):
        nums1.append(nums[i])
    for e in nums1:
        answer = answer + e
        count += 1
        if answer >= target:
            flag = 1
            break
if flag == 0:
    print('0')
else:
    print(count)