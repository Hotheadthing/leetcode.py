s = "ABCD"
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"
# s ="AAAAAAAAAAA"
n = len(s)
print(n)
nMap = {}
arr = []
for i in range(n-9):
    x = s[i]
    for j in range(i+1,i+10):
        x += s[j]
    if x not in nMap:
        nMap.__setitem__(x,1)
    else:
        nMap[x] += 1
print(nMap)
for d in nMap:
    if nMap[d] > 1:
        arr.append(d)
print(arr)




