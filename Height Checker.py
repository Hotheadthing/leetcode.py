import copy
heights = [1,1,4,2,1,3]
heights = [5,1,2,3,4]
heights = [1,2,3,4,5]
origi_height = copy.deepcopy(heights)
heights.sort()

count = 0
for i in range(len(heights)):
    if heights[i] != origi_height[i]:
        count += 1

print(count)