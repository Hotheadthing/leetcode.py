n = 5
arr = []
for i in range(n+1):
    x = bin(i)[2:]
    count = 0
    if x == 0:
        arr.append(0)
    else:
        for j in range(len(x)):
            if x[j] == "1":
                count += 1
        arr.append(count)
print(arr)
