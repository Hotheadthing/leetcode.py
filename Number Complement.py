num = 1
x = bin(num)[2:]
print(x)
z = ""
for i in range(len(x)):
    y = int(x[i])^1
    z = z + str(y)

print(int(z,2))

