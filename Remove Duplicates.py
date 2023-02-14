from collections import deque
s = "bcabc"
s = "cbacdcbc"
# s = "cdadabcc"
hmap = {}
q = deque()

for i in range(len(s)):
    if len(q) == 0:
        q.append(s[i])
        if s[i] not in hmap:
            hmap.__setitem__(s[i],1)
        else:
            hmap[s[i]] += 1

    else:
        if s[i] == q[0]:
            q.popleft()
            q.append(s[i])
        else:
            if s[i] not in hmap:
                hmap.__setitem__(s[i],1)
                q.append(s[i])
            else:
                if s[i] > q[-1]:
                    print(s[i])
                    print(q)
                    q.append(s[i])
                    hmap[s[i]] += 1

print(q)
# arr = []
# print(q)
# print(hmap)
# for i in range(len(q)):
#     if hmap[q[i]] > 1:
#         hmap[q[i]] -= 1
#     else:
#         arr.append(q[i])
#
# print(arr)

