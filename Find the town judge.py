# n = 2
# trust = [[1,2]]
n = 3
trust = [[1,3],[2,3],[3,1]]
n = 3
trust = [[1,3],[2,3]]

n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

n = 1
trust = []

gen_people = {}
trust_box = {}

for i in range(len(trust)):
    if trust[i][1] not in trust_box:
        trust_box.__setitem__(trust[i][1],1)
    else:
        trust_box[trust[i][1]] += 1
    if trust[i][0] not in gen_people:
        gen_people.__setitem__(trust[i][0],1)
    else:
        gen_people[trust[i][0]] += 1

judge = 0
flag = False
for d in trust_box:
    if (trust_box[d] == n-1) and d not in gen_people:
        flag = True
        judge = d
        break
# if (n == 1) or (len(trust) == 0):
#     flag = False
if len(trust) == 0:
    print(n)
elif flag == True:
    print(judge)
else:
    print(-1)


