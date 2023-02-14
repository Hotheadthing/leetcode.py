arr = [2,4,6,8,16]

def find_gcd(a,b):
    while b:
        a, b = b, a % b
    return a


num0 = arr[0]
num1 = arr[1]
gcd = find_gcd(num0,num1)
for i in range(2,len(arr)):
    gcd = find_gcd(gcd,arr[i])
print(gcd)
