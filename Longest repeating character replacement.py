s = "ABAB"
k = 2
s = "AABABBA"
k = 1
s = "ABBB"
k = 2
n = len(s)
l = 0
result = 0
count = {}

for r in range(len(s)):
    if s[r] not in count:
        count.__setitem__(s[r],1)
    else:
        count[s[r]] += 1
    window = r - l + 1
    maximum = 0
    for values in count:
        maximum = max(maximum,count[values])
    if window - maximum <= k:
        result = max(window,result)
    else:
        l += 1
        count[s[l]] -= 1

print(result)
