cost = [10,15,20]
# cost = [1,100,1,1,1,100,1,1,100,1]

cost = [0,0,2,1]
cost = [0,1,1,1]

f_amount = 0
n = len(cost)
l = 0
if n == 2:
    if cost[0] <= cost[1]:
        print(cost[0])
    else:
        print(cost[1])
elif n == 3:
    f_amount = cost[0] + cost[2]
    if cost[1] < f_amount:
        print(cost[1])
    else:
        print(f_amount)
else:
    for i in range(n-1):
        if ((cost[i] < cost[i+1]) and i > l) or (cost[i] < cost[i+1] and i == 0):
            f_amount += cost[i]
            l = i
        elif (cost[i] == cost[i+1]) and i >= l:
            f_amount += cost[i]
            l = i+1
        elif (cost[i] > cost[i+1]) and i > l:
            f_amount += cost[i+1]
            l = i+1
    print(f_amount)

