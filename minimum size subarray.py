target = 7
nums = [2,3,1,2,4,3]
for i in range(1,len(nums)):
    nums[i] = nums[i] + nums[i-1]

print(nums)

l = 0
n = len(nums)
r = n-1


def count(arr,mid,target):
    val = nums[-1]
    for i in range(len(mid)-2,-1,-1):
        if val - nums[i] == target
while l <= r:
    mid = (l+r)//2
    if count(nums,mid,target):
