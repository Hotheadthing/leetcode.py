n = 5
start = 0
arr = []

for i in range(n):
    x = start + (2*i)
    arr.append(x)

z = arr[0]
for i in range(1,len(arr)):
    z = z^arr[i]

print(z)