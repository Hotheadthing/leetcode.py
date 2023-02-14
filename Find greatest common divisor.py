import math
nums = [2,5,6,9,10]
nums = [7,5,6,8,3]
nums = [3,3]
l = max(nums)
s = min(nums)

ans = math.gcd(l,s)
print(ans)