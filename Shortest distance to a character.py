# s = "loveleetcode"
# c = "e"
# s = "aaab"
# c = "b"
s = "baaa"
c = "b"
arr =[]
arr1 = []
r_maxarray = []
l = 0
r = 0
for i in range(len(s)):
    if s[i] == c:
        r_maxarray.append(i)
    else:
        r_maxarray.append(0)
print(r_maxarray)
set = 0
set1 = 0
for i in range(len(r_maxarray)):
    if r_maxarray[i] == 0:
        arr.append(set)
    elif r_maxarray[i] != 0:
        set = r_maxarray[i]
        arr.append(-1)
print(arr)

for j in range(len(r_maxarray)-1,-1,-1):
    if r_maxarray[j] != 0:
        set1 = r_maxarray[j]
        arr1.append(-1)
    else:
        arr1.append(set1)

arr1.reverse()
print(arr1)

for i in range(len(r_maxarray)):
    if r_maxarray[i] == 0:
        if arr[i] == 0:
            r_maxarray[i] = abs(arr1[i] - i)
        else:
            x = min(abs(i-arr[i]),abs(i-arr1[i]))
            r_maxarray[i] = x
    else:
        r_maxarray[i] = 0
print(r_maxarray)

