nums = [1,3,4,2,2]
nums = [2,5,9,6,9,3,8,9,7,1]
slow,fast = 0,0
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break

slow2 = 0
while True:
    slow2 = nums[slow2]
    slow = nums[slow]
    if slow == slow2:
        print(slow)
        break
