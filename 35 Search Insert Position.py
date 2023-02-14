nums = [1,3,5,6]
target = 7
if target in nums:
    a = nums.index(target)
else:
    nums.append(target)
    nums.sort()
    a = nums.index(target)

print(a)