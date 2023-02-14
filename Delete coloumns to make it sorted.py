import copy
strs = ["cba","daf","ghi"]
# strs = ["a","b"]
strs = ["zyx","wvu","tsr"]
strs = ["rrjk","furt","guzm"]
count = 0
arr1 = []
for i in range(len(strs)):
    arr = []
    if len(strs[0]) == 1:
        arr1.append(ord(strs[i]))
    else:
        for j in range(len(strs[0])):
            arr.append(ord(strs[j][i]))
        x = copy.deepcopy(arr)
        arr.sort()
        if x != arr:
            count += 1

if len(arr1) != 0:
    x = copy.deepcopy(arr1)
    arr1.sort()
    if x != arr1:
        count += 1
    print(count)
else:
    print(count)