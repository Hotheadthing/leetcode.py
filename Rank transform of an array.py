import copy
arr = [40,10,20,30]
arr = [100,100,100]
arr = [37,12,28,9,100,56,80,5,12]
x = copy.deepcopy(arr)
arr.sort()
nMap ={}
res = []
count = 0
for j in range(len(x)):
    if arr[j] not in nMap:
        nMap.__setitem__(arr[j],(j+1) - count)
    elif arr[j] in nMap:
        count = 1


for i in range(len(x)):
    res.append(nMap[x[i]])
print(res)