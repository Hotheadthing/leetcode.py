n = 12
output = ""
mod = 1000000007
for i in range(1,n+1):
    output += bin(i)[2:]

x = int(output,2) % mod
print(x)
