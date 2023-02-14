s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
ans = ""

for i in range(len(s)):
    if s[i].isalnum():
        val = s[i].lower()
        ans += val
print(ans == ans[::-1])