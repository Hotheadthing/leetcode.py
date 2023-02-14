x = 0
answer = 0
for i in range(x):
    # print(i)
    if i * i > x:
        answer = i-1
        break
print(answer)

#another example
low = 0
high = x
while low <= high:
    mid = low + (high - low) // 2
    if mid * mid == x:
        print(mid)
    elif mid * mid < x:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)