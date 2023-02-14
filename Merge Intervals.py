# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[0,0]]
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
intervals.sort()
print(intervals)
arr = []
new = []
for i in range(len(intervals)):
    if i == 0:
        new = intervals[i]
    else:
        if intervals[i][0] > new[1]:
            if new not in arr:
                arr.append(new)
            if intervals[i] not in arr:
                arr.append(intervals[i])
        else:
            if intervals[i][0] > new[0]:
                new[1] = max(new[1],intervals[i][1])
            else:
                new[0] = intervals[i][0]
                new[1] = max((new[1],intervals[i][1]))
            if new not in arr:
                arr.append(new)
        new = arr[-1]
        print(arr)
