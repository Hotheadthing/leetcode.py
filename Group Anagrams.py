strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
strs = ["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
# strs = [""]
# strs = ["a"]
arr = []

for i in range(len(strs)):
    val = 0
    hmap = {}
    str = ""
    for j in range(len(strs[i])):
        hmap.__setitem__(strs[i][j],1)
    # print(hmap)
    for x in hmap:
        val += ord(x)
        str += x
    arr.append([val,str,i])

print(arr)
arr.sort()



hmap = {}
for i in range(len(arr)):
    if arr[i][0] not in hmap:
        hmap.__setitem__(arr[i][0],[strs[arr[i][2]]])
    else:
        hmap[arr[i][0]].append(strs[arr[i][2]])

print(hmap)

ans = []

for x in hmap:
    if len(hmap[x]) == 1:
        ans.append(x)
    else:
        for i in range(len(hmap[x])):



