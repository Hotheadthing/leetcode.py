nums = [100,4,200,1,3,2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
nums.sort()
print(nums)

cur_count = 1
final = 0

for i in range(1,len(nums)):
    if nums[i] == nums[i-1] + 1:
        cur_count += 1
    else:
        if cur_count > final:
            final = cur_count
            cur_count = 1
            # print(cur_count,final)
        else:
            cur_count = 1

print(cur_count)
if cur_count > final:
    final = cur_count
print(final)