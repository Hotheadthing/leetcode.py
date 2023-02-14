# nums = [1,2,3,4]
# queries = [[1,0],[-3,1],[-4,0],[2,3]]
nums = [1]
queries = [[4,0]]
arr = []
sum = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        sum += nums[i]
for i in range(len(queries)):
    if nums[queries[i][1]] % 2 == 0:
        sum -= nums[queries[i][1]]
    nums[queries[i][1]] += queries[i][0]
    if nums[queries[i][1]] % 2 == 0:
        sum += nums[queries[i][1]]
    arr.append(sum)
print(arr)