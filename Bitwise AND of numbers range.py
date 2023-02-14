left = 1
right = 2147483647
ans = left
for i in range(left+1,right+1):
    ans = ans & i

print(ans)