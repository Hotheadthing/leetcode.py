nums = [0,1,1]
nums = [1,1,1]
compare = ""
arr = []
for i in range(len(nums)):
    compare += str(nums[i])
    if int(compare,2) % 5 == 0:
        arr.append(True)
    else:
        arr.append(False)

print(arr)