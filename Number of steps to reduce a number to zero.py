num = 123
step = 0
while num != 0:
    if num % 2 == 0:
        num = num // 2
        step += 1
    else:
        num -= 1
        step += 1
print(step)