num = 4009
arr = []
new1 = ""
new2 = ""
for d in str(num):
    arr.append(int(d))

arr.sort()

for i in range(len(arr)):
    if i == 0 or i == 3:
        new1 = new1 + str(arr[i])
    else:
        new2 = new2 + str(arr[i])

ans = int(new1) + int(new2)
print(ans)