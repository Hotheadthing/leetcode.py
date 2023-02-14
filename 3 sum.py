nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [-2,0,1,1,2]
nums.sort()
print(nums)
n = len(nums)
ans = []
for i, a in enumerate(nums):
    if i > 0 and a == nums[i-1]:
        continue

    l = i+1
    r = n-1
    while l < r:
        threesum = a + nums[l] + nums[r]

        if threesum > 0:
            r -= 1
        elif threesum < 0:
            l += 1
        else:
            ans.append([a,nums[l],nums[r]])
            l += 1
            while nums[l] == nums[l-1] and l < r:
                l += 1

print(ans)


























# for i in range(n):
#     val = -nums[i]
#     l = i+1
#     r = n-1
#     arr = []
#     while l < r:
#         if val == nums[l] + nums[r]:
#             arr.append(-val)
#             arr.append(nums[l])
#             arr.append(nums[r])
#             if arr not in ans:
#                 ans.append(arr)
#                 arr = []
#             else:
#                 arr = []
#             r -= 1
#         elif val > nums[l] + nums[r]:
#             l += 1
#         else:
#             r -= 1
#     if len(arr) != 0:
#         ans.append(arr)
#
# print(ans)
