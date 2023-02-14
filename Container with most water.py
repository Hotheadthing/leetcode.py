height = [1,8,6,2,5,4,8,3,7]
height = [1, 1]
l = 0
n = len(height)
r = n-1
capacity = 0
while l < r:
    trap = min(height[l],height[r])
    distance = r - l
    capacity = max(capacity,trap*distance)

    if height[l] <= height[r]:
        l += 1
    else:
        r -= 1

print(capacity)


