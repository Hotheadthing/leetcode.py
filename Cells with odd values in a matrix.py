m = 2
n = 3
indices = [[0,1],[1,1]]
m = 2
n = 2
indices = [[1,1],[0,0]]

arr = []
for i in range(m):
    q = []
    for j in range(n):
        q.append(0)
    arr.append(q)
print(arr)

for i in range(len(indices)):
    j = indices[i][0]
    k = indices[i][1]
    arr[j][k] += 1
    for m in range(len(arr)):
        for n in range(len(arr[0])):
            if m == j:
                arr[m][n] += 1
            elif n == k:
                arr[m][n] += 1
print(arr)
count = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] % 2 != 0:
            count += 1
print(count)

