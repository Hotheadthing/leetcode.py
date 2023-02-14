nums = [5,6,7,8,9]
X = 4
X1 = X
count = 0
count2 =0
# flag1 = 'true'
# flag2 = 'true'
# for digit in nums:
#     if digit > X:
#         flag1 = 'true'
#     else:
#         flag2 = 'false'

for i in range (len(nums)):
    if nums[i] > X:
        break
    elif X - nums[i] != 0 and X - nums[i] > 0:
        count += 1
        X = X - nums[i]
       # print(f"In loop {count}")
    elif X - nums[i] ==0:
        count += 1
        X = X - nums[i]
           # print(f"The value of count is : {count}")
        break

if X != 0:
   for j in range(len(nums) - 1, -1, -1):
       if nums[j] > X:
           break
       elif X - nums[j] != 0 and X - nums[j] > 0:
           count += 1
           # print(count)
           X = X - nums[j]
       elif X - nums[j] ==0:
           count += 1
           # print(count)
           X = X - nums[j]
# print(f"the value of X is : r {X}")
if X != 0:
    count = -1

for j in range (len(nums)-1,-1,-1):
    if nums[j] > X1:
        break
    elif X1 - nums[j] != 0 and X1 - nums[j] > 0:
        count2 += 1
        X1 = X1 - nums[j]
        # print(f"zzz..{count2}")
    elif X1-nums[j] == 0:
        count2 += 1
        X1 = X1 - nums[j]
        # print(f"The value of count2 is : {count2}")
        break

if X1 != 0:
   for i in range(len(nums)):
       if nums[i] > X1:
           break
       elif X1 - nums[i] != 0 and X1 - nums[i] > 0:
          count2 += 1
          X1 = X1 - nums[i]
          # print(count2)
       elif X1 - nums[i] == 0:
          count2 += 1
          X1 = X1 - nums[i]
          # print(count2)
# print(f"The value of count2 is : r {count2}")
if X1 != 0:
    count2 = -1
#
# if flag1 == flag2:
#     print('-1')
# else:
if count > count2:
  print(count2)
else:
  print(count)

