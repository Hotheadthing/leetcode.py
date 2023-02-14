allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
mMap = {}
for i in range(len(allowed)):
    if allowed[i] not in mMap:
        mMap.__setitem__(allowed[i],1)
    else:
        mMap[allowed[i]] += 1
count = 0
for i in range(len(words)):
    flag = False
    for j in range(len(words[i])):
        if words[i][j] in mMap and mMap[words[i][j]] != 0:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        count += 1
print(count)

