import copy
nums = [1,2,3,4,5,6,7]
k = 3
nums = [-1,-100,3,99]
k = 2
nums = [1,2]
k = 3
n = len(nums)
result = n - k
# x = nums[result:]
# nums = copy.deepcopy(nums[:result])
# ans = x + nums
# nums = copy.deepcopy(ans)
# print(nums)

for i in range(k):
    temp = nums[-1]
    nums.remove(nums[-1])
    nums.insert(0,temp)

# for i in range(k):
#     nums.insert(0,arr[i])
#
print(nums)




