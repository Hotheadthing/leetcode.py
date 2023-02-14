candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
print(candidates)
arr = []

for i in range(len(candidates)):
    q = []
    s = candidates[i]
    for j in range(i+1,len(candidates)):
        s += candidates[j]
        print(s,candidates[i],candidates[j])
        if s > target:
            break
        elif s == target:
            q.append(i)
            q.append(j)
            arr.append(q)
            break
print(arr)