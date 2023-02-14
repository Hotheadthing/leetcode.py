num = 4
count = 0

for i in range(1, num+1):
    x = 0
    p = str(i)
    for j in range(len(p)):
        x += int(p[j])
    if x % 2 == 0:
        count += 1
print(count)

