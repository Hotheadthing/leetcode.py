arr = [1,2,3,4,5]
k = 4
x = 3
arr = [1,2,3,4,5]
k = 4
x = -1
ans = []
if x <= arr[0]:
    ans = arr[0:k]
elif x > arr[-1]:
    count = k
    chn_count = 0
    for i in range(len(arr)-1,-1,-1):
        ans.append(arr[i])
        chn_count += 1
        if chn_count == count:
            break
else:
    ref_count = 0
    for i in range(len(arr)):
        ref_count += 1
        if arr [i] == x:
            if ref_count == k:
                ans = arr[0:k+1]
            elif k < ref_count:
                ans = arr[ref_count-k:k+1]
            else:
                ans = arr[0:ref_count]
                # print(ans)
                extra = k - ref_count
                # print(extra)
                z = ref_count - 1
                for i in range(extra):
                    # print(arr[i])
                    ans.append(arr[z + 1 ])
                    z += 1

print(ans)

