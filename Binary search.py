nums = [-1,0,3,5,9,12]
target = 9
n = len(nums)
l = 0
r = n-1
while l <= r:
    mid = (l+r) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l += 1
    else:
        r -= 1