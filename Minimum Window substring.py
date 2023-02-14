s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"
s = "a"
t = "aa"
s = "ab"
t = "a"
l = 0
mapt = {}

for chr in t:
    if chr not in mapt:
        mapt.__setitem__(chr,1)
    else:
        mapt[chr] += 1

maps = {}
result = 9999999999999
string = ""
for r in range(len(s)):
    if s[r] in mapt:
        if s[r] not in maps:
            maps.__setitem__(s[r],1)
        else:
            maps[s[r]] += 1
    if len(mapt) == len(maps):
        flag = True
        for val in mapt:
            if maps[val] < mapt[val]:
                flag = False
        if flag:
            # print(l,r)
            while flag:
                if r - l + 1 < result:
                    result = r - l + 1
                    string = s[l:r+1]
                if s[l] in maps:
                    maps[s[l]] -= 1
                    if maps[s[l]] < mapt[s[l]]:
                        flag = False
                l += 1
            if l >= len(s):
                break
            while s[l] not in mapt:
                l += 1
                if l >= len(s):
                    break

print(string)











    # if mapt in maps:
    #     print(l,r)
    #     while mapt in maps:
    #         if r - l + 1 < result:
    #             result = r - l + 1
    #             string = s[l:r+1]
    #         maps[s[l]] -= 1
    #         l += 1
    #     print(maps,mapt)
    #     while s[l] not in mapt:
    #         l += 1

