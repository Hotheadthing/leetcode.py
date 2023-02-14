num = "35427"
arr = []
ans = ""
for d in num:
    arr.append(d)
j = -999999999999
for i in range(len(arr)-1,-1,-1):
    if int(arr[i]) % 2 != 0:
        j = i
        break

if j != -999999999999:
    x = arr[:j+1]
    for i in range(len(x)):
        ans = ans + x[i]
    print(ans)
else:
    print("")


