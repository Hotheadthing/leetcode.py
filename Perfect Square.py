num = 14
l = 0
r = num

while l <= r:
    mid = (l+r)//2
    print(mid)
    if mid * mid == num:
        print(True)
        break
    elif mid * mid > num:
        r = mid - 1
    else:
        l = mid + 1
