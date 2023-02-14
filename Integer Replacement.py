import copy
n = 10000
m = copy.deepcopy(n)
v = 0
v1 = 0
while n != 1:
    if n % 2 == 0:
        v += 1
        n = n//2
    else:
        v += 1
        n = n - 1

while m != 1:
    if m % 2 == 0:
        m = m//2
        v1 += 1
    else:
        m = m + 1
        v1 += 1

print(v,v1)
# print(min(v,v1))