# s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
# s = "dvdf"
l = 0
r = 1
n = len(s)
hmap = {}
hmap.__setitem__(s[0],1)
ans = 1
result = 0
while r < n:
    if s[r] not in hmap:
        hmap.__setitem__(s[r],1)
        ans += 1
        r += 1
    else:
        result = max(ans,result)
        ans = 1
        hmap = {}
        l += 1
        hmap.__setitem__(s[l],1)
        r = l+1

result = max(result,ans)
print(result)
