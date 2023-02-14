arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
arr.sort()
#print(arr)
n = len(arr)
m = n * 0.05
m = int(m)
#print(m)

for i in range(m):
    arr.pop(-1)

x = arr[m:]
#print(x)

length = len(x)
summation = 0

for i in range(length):
    summation += x[i]
print(summation/length)