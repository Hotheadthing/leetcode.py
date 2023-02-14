strs = ["flower","flow","flight","flam"]
prefix = strs[0]
output = ""
for elements in strs[1:]:
    while elements[0:len(prefix)] != prefix:
        prefix = prefix[:len(prefix)-1]
        if not prefix:
            break

output = prefix
print(output)