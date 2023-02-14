encoded = [1,2,3]
first = 1
encoded = [6,2,7,3]
first = 4
arr = []
for i in range(len(encoded)):
    if i == 0:
        arr.append(first)
        first = first^encoded[i]
        arr.append(first)
    else:
        arr.append(first^encoded[i])
        first = first^encoded[i]

print(arr)


