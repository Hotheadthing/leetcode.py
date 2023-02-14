nums1 = [1,2,3]
nums2 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
nMap = {}
mMap = {}

for i in range(len(nums1)):
    if nums1[i] not in nMap:
        nMap.__setitem__(nums1[i],1)
    else:
        nMap[nums1[i]] += 1

for j in range(len(nums2)):
    if nums2[j] not in mMap:
        mMap.__setitem__(nums2[j],1)
    else:
        nMap[nums2[j]] += 1
arr = []
narr = []
marr = []
print(nMap)
print(mMap)
for d in nMap:
    if d not in mMap:
        narr.append(d)

for d in mMap:
    if d not in nMap:
        marr.append(d)

print(narr)
print(marr)
arr.append(narr)
arr.append(marr)
print(arr)