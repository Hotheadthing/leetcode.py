arr = [17,18,5,4,6,1]
arr = [400]
curr_max = 0

for i in range(len(arr)-1,-1,-1):
    if i == len(arr)-1:
        curr_max = arr[i]
        arr[i] = -1
    else:
        if arr[i] > curr_max:
            temp = arr[i]
            arr[i] = curr_max
            curr_max = temp
        else:
            arr[i] = curr_max
print(arr)