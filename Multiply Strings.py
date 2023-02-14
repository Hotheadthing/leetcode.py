import math
num1 = "123"
num2 = "456"
arr1 = []
arr2 = []

mMap = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0
      }

for i in range(len(num1)):
    arr1.append(mMap[num1[i]])

for i in range(len(num2)):
    arr2.append(mMap[num2[i]])

ans1 = 0
ans2 = 0

for i in range(len(arr1)-1,-1,-1):
    ans1 += arr1[i] * (10**(len(arr1)-(i+1)))

for i in range(len(arr2)-1,-1,-1):
    ans2 += arr2[i] * (10**(len(arr2)-(i+1)))


print(ans1*ans2)
print(math.fa)