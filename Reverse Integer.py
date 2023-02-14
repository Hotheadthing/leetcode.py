x = 120
sign = 1

if x < 0:
    sign = -1

x = abs(x)
y = str(x)
z = ""

for i in range(len(y)-1,-1,-1):
    z += y[i]

z = int(z)

ans = z * sign
print(ans)

print(2**31)