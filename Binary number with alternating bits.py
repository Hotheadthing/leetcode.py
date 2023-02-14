n = 11
x = bin(n)[2:]
flag = True
if len(x) == 1:
    print(False)
else:
    for i in range(len(x)-1):
        if x[i+1] == x[i]:
            flag = False
            break

print(flag)
