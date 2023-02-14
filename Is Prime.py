import math
import sys
sys.setrecursionlimit(10**6)
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if (n % 2 == 0) or (n % 3 == 0):
        return False

    i = 5
    while i * i < n:
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        i += 6
    return True

x = prime(31)
print(x)

# Fastest Way: TC- O(log(n))
def is_prime(a):
    if a <= 1:
        return False
    else:
        for i in range(2,math.floor(math.sqrt(a)+1)):
            if a % i == 0:
                return False
            return True

z = prime(1)
print(z)


