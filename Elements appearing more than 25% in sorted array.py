arr = [1,2,2,6,6,6,6,7,10]
arr = [1,1]
n = len(arr)
x = n//4
mMap = {}

for i in range(len(arr)):
    if arr[i] not in mMap:
        mMap.__setitem__(arr[i],1)
    else:
        mMap[arr[i]] += 1

for d in mMap:
    if mMap[d] > x:
        print(d)
        break