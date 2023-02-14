s = "ababcbacadefegdehijhklij"
temp_arr = []
arr = []
index = 0

for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            index = j
        
    temp_arr = s[i:index]
    print(temp_arr)
    print(index,s[index])

