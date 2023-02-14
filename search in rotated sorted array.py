nums = [4,5,6,7,0,1,2]
target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
nums = [1]
target = 0
nums = [1,3]
target = 3
nums = [4,5,6,7,8,1,2,3]
target = 8
nums = [5,1,3]
target = 5
n = len(nums)
l = 0
r = n-1

while l < r:
    mid = (l+r)//2
    print(l,r,mid,nums[mid])
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        if target < nums[l]:
            l = mid+1
            if nums[l]== target:
                print(l)
                break
        elif target > nums[l]:
            r = mid - 1
        else:
            print(l)
            break
    else:
        l = mid+1
        if nums[l] == target:
            print(l)
            break

