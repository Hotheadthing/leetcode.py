points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
x_max = -52
y_max = -52

for i in range(len(points)):
    x_max = max(x_max,points[i][1])
    y_max = max(y_max,points[i][0])

area = 0.5 * x_max * y_max
print(area)