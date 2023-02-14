# from collections import OrderedDict
# nums = [1,2,1,2,3,1]
# k = 2
nums = [1]
k = 1
nums = [-1,-1]
k = 1
nums = [3,0,1,0]
k = 1
hmap = {}

for x in nums:
    if x not in hmap:
        hmap.__setitem__(x,1)
    else:
        hmap[x] += 1

print(hmap)

arr = []
for x in hmap:
    arr.append([x,hmap[x]])

arr.sort(key=lambda x:x[1],reverse=True)
print(arr)

ans = []
for i in range(k):
    ans.append(arr[i][0])

print(ans)




