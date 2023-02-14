matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
l = 999999999999
r = -99999999999
for i in range(len(matrix)):
    l = min(l,matrix[i][0])
    r = max(r,matrix[i][-1])

print(l,r)

def count(arr,mid,target):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] < mid:
                count += 1
            else:
                break
    return count
ans = 0
while l <= r:
    mid = (l+r)//2
    x = count(matrix,mid,k)
    print(mid,x)
    if count(matrix,mid,k) == mid:
        print(mid)
        break
    elif count(matrix,mid,k) > mid:
        r = mid - 1
    else:
        l = mid + 1


