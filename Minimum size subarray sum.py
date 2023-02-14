from collections import deque

queue = deque()
target = 11
nums = [1,1,1,1,1,1,1,1]


min_len = 9999999999
cur_sum = 0
for i in range(len(nums)):
    queue.append(nums[i])
    cur_sum += nums[i]
    if cur_sum >= target:
        min_len = min(min_len,len(queue))
        while cur_sum >= target:
            val = queue.popleft()
            cur_sum = cur_sum - val
            if cur_sum >= target:
                min_len = min((min_len),len(queue))


if min_len == 9999999999:
    print(0)
else:
    print(min_len)
