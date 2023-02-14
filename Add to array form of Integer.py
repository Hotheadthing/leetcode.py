num = [1,2,0,0]
k = 34
link = ""
for d in num:
    link += str(d)
ans = k + int(link)
arr = []
ans = str(ans)
for i in range(len(ans)):
    arr.append(int(ans[i]))
print(arr)