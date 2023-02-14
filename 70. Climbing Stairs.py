n = 7
ways = 0
count = 0
if n == 0:
    pass
elif n % 2 != 0:
    ways += 1
    n = n//2
    ways = ways + n
    for z in range(n):
        n = n - z
        for i in range(n-1):
            n = n*(i+1)
        for j in range (ways-1):
            ways = ways*(j+1)
    ways = ways // n
print(ways)
# elif n % 2 ==0:
#     ways += 1
#     n = n // 2


# print(n)