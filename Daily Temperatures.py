from collections import deque

temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
# temperatures = [30,60,90]
# temperatures = [55,38,53,81,61,93,97,32,43,78]
temperatures = [34,80,80,34,34,80,80,80,80,34]

res = [0 for i in range(len(temperatures))]
stack = []

for i,temp in enumerate(temperatures):
    while stack and temp > stack[-1][1]:
        index, temperature = stack.pop()
        res[index] = i - index
    stack.append([i, temp])

print(res)