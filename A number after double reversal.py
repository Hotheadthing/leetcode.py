num = 526
arr = []
new1 = ""
for d in str(num):
    arr.append(int(d))
arr.reverse()

for i in range(len(arr)):
    new1 = new1 + str(arr[i])

z = int(new1)
print(z)
arr1 = []
new2 = ""
for d in str(z):
    arr1.append(int(d))
arr1.reverse()
for i in range(len(arr1)):
    new2 = new2 + str(arr1[i])
y = int(new2)
print(y)
if num == y:
    print(True)
else:
    print(False)

