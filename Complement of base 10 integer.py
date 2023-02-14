n = 10
x = bin(n)[2:]
y = ""

for i in range(len(x)):
    z = (1^int(x[i]))
    y = y + str(z)

print(int(y,2))