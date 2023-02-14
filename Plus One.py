digits = [1,2,3]
output = []
res = int("".join(map(str, digits)))
res = res + 1
res1 = [int(x) for x in str(res)]
print(res1)

