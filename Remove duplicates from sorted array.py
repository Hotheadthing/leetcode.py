nums = [1,1,2,2,2,2,2,2,2,2]
i = nums[0]
for digits in nums[1:]:
    # print(digits)
    if digits == i:
        nums.remove(digits)
        # nums = nums.remove(digits)
        # print(nums)
    else:
        i = digits
        # print(i)
print(nums)
