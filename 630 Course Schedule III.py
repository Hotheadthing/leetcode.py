courses = [[3,2],[4,3]]
data = []
duration =[]
count = 0
value = 0

for a in range(len(courses)-1,-1,-1):
    # print(a)
    if courses[a][0] > courses[a][1]:
        del courses[a]
# print(courses)
if courses == []:
    print(0)
else:
    for i in range(len(courses)):
        data.append(courses[i][0])
        data.sort()
    # print(data)
    for j in range(len(courses)):
        duration.append(courses[j][1])
        duration.sort()
    # print(duration)
    for q in range(len(data)):
        value += data[q]
        if value <= duration[-1]:
            count += 1
    print(count)


