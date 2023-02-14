from collections import deque
s = "([)]"
# s = "()"
s = "()[]{}"
s = "(]"
arr = deque()
closing = {")","}","]"}
opening = {"(","[","{"}
for i in range(len(s)):
    if s[i] in closing and len(arr) == 0:
        print(False)
        break
    elif s[i] in opening:
        arr.append(s[i])
    else:
        if s[i] == ")" and arr[-1] == "(":
            arr.pop()
        elif s[i] == "}" and arr[-1] == "{":
            arr.pop()
        elif s[i] == "]" and arr[-1] == "[":
            arr.pop()
        else:
            print(False)
            break

print(arr)

























# dictionary = {"(": ")", "[": "]", "{": "}"}

# for digit in s:
#     if str(dictionary.get(digit)) in s:
#         a = s.index(dictionary.get(digit))
#         b = s.index(digit)
#         r = a-b
#         if r % 2 ==0:
#             print('false')
#             break
#         else:
#             print('true')

