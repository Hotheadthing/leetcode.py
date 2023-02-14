nums = [2,1,4,3]
left = 2
right = 3
# nums = [2,9,2,5,6]
# left = 2
# right = 8
number = 0
j = 0
for i in range(len(nums)):
    if (left >= nums[i] or left <= nums[i]<= right) and nums[i] <= right:
        j += 1
    else:
        number += (j*(j+1))//2
        j = 0
    if i == len(nums)-1:
        if j != 0:
            number += (j-1*(j))//2
    print(j,nums[i])
print(number)