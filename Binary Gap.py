n = 5
x = bin(n)[2:]
i = 0
cur_count = 0
flag = 1
for k in range(len(x)):
    if flag == 1 and x[k] == "1":
        i = k
        flag = 2
    if flag == 2 and x[k] == "1":
        cur_count = max(cur_count,k-i)
        i = k
print(cur_count)

