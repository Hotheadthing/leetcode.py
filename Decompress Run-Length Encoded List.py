nums = [1,2,3,4]
nums = [1,1,2,3]
arr = []
for i in range(0,len(nums),2):
    for j in range(nums[i]):
        arr.append(nums[i+1])
print(arr)
