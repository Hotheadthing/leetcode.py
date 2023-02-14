nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
nums = [2,1]
B = nums[0]
n = len(nums)
l = 0
r = n-1

poc = 0

while l <= r:
    mid = (l+r)//2
    if (nums[mid] >= B) and (nums[mid] > nums[-1]):
        l = mid + 1
    else:
        poc = nums[mid]
        r = mid - 1
print(poc)



