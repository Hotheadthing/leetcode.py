num1 = 0
num2 = 1

count = 0

if num1 == 0 or num2 == 0:
    print(max(num1, num2))
else:
    for i in range(max(num2, num1)):
        if num2 > num1:
            num2 = num2 - num1
            count += 1
            if num2 == 0:
                break
        else:
            num1 = num1 - num2
            count += 1
            if num1 == 0:
                break
    print(count)

