n = 2
res = []
for i in range(2**n):
    res.append(i^(i>>1))
print(res)