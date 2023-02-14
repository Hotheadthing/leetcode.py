nums = [1,2,2,3]
# nums = [6,5,4,4]
# nums = [1,3,2]
nums1 = []
for d in nums:
    nums1.append(d)
nums1.sort()
n = nums1
flag = False
if nums == n:
    flag = True

nums1.sort(reverse=True)
m = nums1
flag1 = False
if nums == m:
    flag1 = True

if flag1 == True or flag == True:
    print(True)
else:
    print(False)

