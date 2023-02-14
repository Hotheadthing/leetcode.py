# licensePlate = "1s3 PSt"
# words = ["step","steps","stripe","stepple"]
# licensePlate = "1s3 456"
# words = ["looks","pest","stew","show"]
licensePlate = "GrC8950"
words = ["according","level","meeting","none","marriage","rest"]
lMap ={}

for i in range(len(licensePlate)):
    if licensePlate[i].isalpha():
        x = licensePlate[i].lower()
        if x not in lMap:
            lMap.__setitem__(x,1)
        else:
            lMap[x] += 1
print(lMap)

result = 99999999
ans = ""
for i in range(len(words)):
    comp_map = {}
    for j in range(len(words[i])):
        if words[i][j] not in comp_map:
            comp_map.__setitem__(words[i][j],1)
        else:
            comp_map[words[i][j]] += 1
    flag = True
    for d in lMap:
        if d in comp_map:
            if lMap[d] > comp_map[d]:
                flag = False
                break
        else:
            flag = False
            break

    if flag == True:
        if len(words[i]) < result:
            result = len(words[i])
            ans = words[i]

print(ans)

