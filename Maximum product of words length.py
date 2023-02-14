words = ["abcw","baz","foo","bar","xtfn","abcdef"]
arr = []
nMap = {}

for i in range(len(words)):
    if words[i] not in nMap:
        nMap.__setitem__(words[i],len(words[i]))
        arr.append(len(words[i]))

print(nMap)
print(arr)
arr.sort(reverse=True)
print(arr)
arr1 = []
product = 0

for i in range(len(arr)):
    for d in nMap:
        if nMap[d] == arr[i] and d not in arr1:
            arr1.append(d)
print(arr1)
