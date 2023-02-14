bills = [5,5,5,10,20]
bills = [5,5,10,10,20]
bills = [5,5,5,10,5,5,10,20,20,20]
count5 = 0
count10 = 0
count20 = 0
flag = True
for i in range(len(bills)):
    if bills[i] == 5:
        count5 += 1
    elif bills[i] == 10:
        count10 += 1
        if count5 >= 1:
            count5 -= 1
        else:
            flag = False
            break
    else:
        count20 += 1
        if count10 >= 1 and count5 >= 1:
            count5 -= 1
            count10 -= 1
        elif count5 >= 3:
            count5 -= 3
        else:
            flag = False
            break
print(flag)




