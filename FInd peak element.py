nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
# nums = [2,1]
# nums = [1,2,3,1]
# nums = [1,2]
# nums = [1,2,3]
# nums = [1,2,3,4,3,2,1]
nums = [0,1,0]
nums = [0,2,1,0]
n = len(nums)
l = 0
r = n-1
ans = 0
while l < r:
    mid = (l+r)//2
    if nums[mid]> nums[mid-1] and nums[mid] > nums[mid+1]:
        ans = mid
    if nums[mid] < nums[mid+1]:
        l = mid + 1
    else:
        r = mid - 1

    if nums[r] > nums[ans]:
        ans = r
print(ans)


