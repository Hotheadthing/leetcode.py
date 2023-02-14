matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
matrix = [[1]]
target = 2
rows = len(matrix)
colms = len(matrix[0])

decid_row = 0
ud = 0
ld = rows - 1

while ud < ld:
    mid = (ud+ld)//2
    if matrix[mid][-1] == target:
        print("True")
        break
    elif matrix[mid][-1] < target:
        ud += 1
    else:
        ld -= 1

print(ud)
l = 0
r = colms - 1
while l <= r:
    mid = (l+r)//2
    if matrix[ud][mid] == target:
        print("True")
        break
    elif matrix[ud][mid] < target:
        l += 1
    else:
        r -= 1


