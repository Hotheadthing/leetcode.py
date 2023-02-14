arr = [2,6,4,1]
arr = [1,2,34,3,4,5,7,23,12]
count = 0
flag = False
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        count += 1
        if count == 3:
            flag = True
            break
    else:
        count = 0
print(flag)