nums = [-1,1,1,2,3,3,4,4,8,8,-1]
nums = [3,3,7,7,10,11,11]
# nums = [1,1,2]
n = len(nums)
l = 0
r = n-1

while l <= r:
    mid = (l+r)//2
    if mid == 0:
        if nums[mid] == nums[mid+1]:
            x = mid + 1
            if x % 2 != 0:
                l = mid + 1
            else:
                r = mid - 1
        else:
            print(nums[mid])
            break
    if mid == (n-1):
        if nums[mid] == nums[mid-1]:
            x = mid
            if x % 2 != 0:
                l = mid + 1
            else:
                r = mid - 1
        else:
            print(nums[mid])
            break
    if nums[mid] == nums[mid-1] or nums[mid] == nums[mid+1]:
        if nums[mid] == nums[mid-1]:
            x = mid
            if x % 2 != 0:
                l = mid + 1
            else:
                r = mid - 1
        else:
            x = mid + 1
            if x % 2 != 0:
                l = mid + 1
            else:
                r = mid - 1
    else:
        print(nums[mid])
        break
