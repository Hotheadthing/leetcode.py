s = "a"
t = "aa"
nMap = {}

for i in range(len(s)):
    if s[i] not in nMap:
        nMap.__setitem__(s[i], 1)
    else:
        nMap[s[i]] += 1

for j in range(len(t)):
    if t[j] in nMap:
        nMap[t[j]] -= 1
        if nMap[t[j]] == 0:
            nMap.pop(t[j])
    elif t[j] not in nMap:
        print(t[j])
