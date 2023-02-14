n = 8
l = 0
r = n
ans = 0
while l <= r:
    mid = (l+r)//2
    count = 0
    for i in range(mid):
        count += (i + 1)
    if count < n:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid
print(ans-1)