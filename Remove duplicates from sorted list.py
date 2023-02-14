head = [1,1,2]
head.sort()
j = 0
for i in head:
    if i in head[j+1:]:
        # head.remove(i)
        del head[i]
        j += 1
    else:
        j += 1
print(head)

