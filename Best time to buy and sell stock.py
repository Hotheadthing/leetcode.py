from collections import deque
q = deque()
prices = [7,1,5,3,6,4]
q.append(prices[0])

for price in range(1,len(prices)):
    print(price)