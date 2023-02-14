x = 3
y = 1

x_bin = bin(x)[2:]
y_bin = bin(y)[2:]

print(x_bin)
x_arr = []
for d in x_bin:
    x_arr.append(d)
print(y_bin)
y_arr = []
for d in y_bin:
    y_arr.append(d)

print(x_arr)
print(y_arr)

if len(y_bin) > len(x_bin):
    for i in range(len(y_bin)-len(x_bin)):
        x_arr.insert(0,'0')
elif len(x_bin) > len(y_bin):
    for i in range(len(x_bin) - len(y_bin)):
        y_arr.insert(0,'0')

count = 0
print(x_arr)
print(y_arr)
for i in range(len(x_arr)):
    if x_arr[i] != y_arr[i]:
        count += 1

print(count)
