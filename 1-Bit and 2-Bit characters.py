bits = [1,0,0]
bits = [1,1,1,0]
l = 0

flag = True
for i in range(len(bits)):
    if bits[i] == 1:
        if i >= l:
            l = i + 2
            if l > len(bits) - 1:
                flag = False
print(flag)
print(l)