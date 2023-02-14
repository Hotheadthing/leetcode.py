arr = [1,2,2,1,1,3]
arr = [1,2]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
nMap ={}

for i in range(len(arr)):
    if arr[i] not in nMap:
        nMap.__setitem__(arr[i],1)
    else:
        nMap[arr[i]] += 1

print(nMap)
s = []
flag = True
for d in nMap:
    if nMap[d] not in s:
        s.append(nMap[d])
    else:
        flag = False
        break
print(flag)
