# First Way. TC:- O(min(a,b)) SC:- O(1) : Repeated subtraction
a = 98
b = 56
result = min(a,b)

while result:
    if a % result == 0 and b % result == 0:
        break
    result -= 1

print(result)

# Second Way. TC:- O(min(a,b)) SC:- O(n): Euclidean Algorithm
def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

y = gcd(98,56)
print(y)

# Modulo Operator in Euclidean Algorithm. TC:-O(min(log(a,b)) and SC same as Euclidean

def GCD(a,b):
    if a == 0:
        return b
    if a > b:
        return GCD(a % b, b)
    elif b > a:
        return GCD(b % a, a)

z = GCD(11, 13)
print(z)

