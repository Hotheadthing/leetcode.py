words = ["cat","bt","hat","tree"]
chars = "atach"
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
O_map = {}

for i in range(len(chars)):
    if chars[i] not in O_map:
        O_map.__setitem__(chars[i],1)
    else:
        O_map[chars[i]] += 1
print(O_map)
count = 0
for i in range(len(words)):
    cmap = {}
    for j in range(len(words[i])):
        if words[i][j] not in cmap:
            cmap.__setitem__(words[i][j],1)
        else:
            cmap[words[i][j]] += 1
    flag = True
    for d in cmap:
        if (d not in O_map) or cmap[d] > O_map[d]:
            flag = False
            break
    if flag == True:
        count += len(words[i])

print(count)
